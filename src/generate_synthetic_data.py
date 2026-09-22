from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
rng = np.random.default_rng(SEED)

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

N_ACCOUNTS = 180

accounts = pd.DataFrame({
    "account_id": [f"A{i:04d}" for i in range(1, N_ACCOUNTS + 1)],
    "account_name": [f"Client_{i:03d}" for i in range(1, N_ACCOUNTS + 1)],
    "region": rng.choice(
        ["North America", "APAC", "Europe"],
        N_ACCOUNTS,
        p=[0.45, 0.35, 0.20],
    ),
    "industry": rng.choice(
        ["Gaming", "E-commerce", "Beauty", "Consumer Apps", "SaaS"],
        N_ACCOUNTS,
    ),
    "tier": rng.choice(
        ["Enterprise", "Mid-Market", "SMB"],
        N_ACCOUNTS,
        p=[0.30, 0.45, 0.25],
    ),
    "acquisition_channel": rng.choice(
        ["Agency", "Direct Sales", "Partner Referral", "Inbound"],
        N_ACCOUNTS,
    ),
    "signup_date": pd.to_datetime(
        rng.choice(
            pd.date_range("2023-01-01", "2025-06-01", freq="7D"),
            N_ACCOUNTS,
        )
    ),
})

base_acv = np.where(
    accounts["tier"].eq("Enterprise"),
    180000,
    np.where(accounts["tier"].eq("Mid-Market"), 75000, 25000),
)

accounts["annual_contract_value"] = np.round(
    base_acv * rng.uniform(0.6, 1.6, N_ACCOUNTS),
    0,
)
accounts.to_csv(RAW / "accounts.csv", index=False)

months = pd.date_range("2024-01-01", "2025-12-01", freq="MS")
performance_rows = []

for _, account in accounts.iterrows():
    base_revenue = account["annual_contract_value"] / 12
    monthly_growth = rng.normal(0.012, 0.02)
    account_health = rng.uniform(0.8, 1.2)

    for month_index, month in enumerate(months):
        seasonality = (
            1.12
            if month.month in [10, 11, 12]
            else 0.92
            if month.month in [1, 2]
            else 1.0
        )
        trend = (1 + monthly_growth) ** month_index
        noise = max(0.55, rng.normal(1, 0.12))

        revenue = max(
            250,
            base_revenue * seasonality * trend * noise * account_health,
        )
        ad_spend = max(100, revenue / rng.uniform(2.0, 5.0))
        impressions = int(ad_spend * rng.uniform(60, 140))
        ctr = rng.uniform(0.008, 0.03)
        clicks = max(1, int(impressions * ctr))
        conversion_rate = rng.uniform(0.01, 0.08)
        conversions = max(1, int(clicks * conversion_rate))

        performance_rows.append(
            [
                account["account_id"],
                month.date(),
                round(revenue, 2),
                round(ad_spend, 2),
                impressions,
                clicks,
                conversions,
            ]
        )

performance = pd.DataFrame(
    performance_rows,
    columns=[
        "account_id",
        "month",
        "revenue",
        "ad_spend",
        "impressions",
        "clicks",
        "conversions",
    ],
)

performance["roas"] = (
    performance["revenue"] / performance["ad_spend"]
).round(2)
performance["ctr"] = (
    performance["clicks"] / performance["impressions"]
).round(4)
performance["conversion_rate"] = (
    performance["conversions"] / performance["clicks"]
).round(4)

performance.to_csv(RAW / "monthly_performance.csv", index=False)

stages = [
    "Discovery",
    "Qualified",
    "Proposal",
    "Negotiation",
    "Closed Won",
    "Closed Lost",
]
stage_probabilities = [0.13, 0.18, 0.20, 0.16, 0.22, 0.11]

opportunity_rows = []
opportunity_number = 1

for _, account in accounts.iterrows():
    number_of_opportunities = rng.integers(1, 5)

    for _ in range(number_of_opportunities):
        created_date = pd.Timestamp(
            rng.choice(
                pd.date_range("2024-01-01", "2025-12-15", freq="D")
            )
        )
        stage = rng.choice(stages, p=stage_probabilities)
        amount = round(
            account["annual_contract_value"] * rng.uniform(0.15, 0.8),
            2,
        )
        days_open = int(rng.integers(5, 140))
        expected_close_date = created_date + pd.Timedelta(days=days_open)

        opportunity_rows.append(
            [
                f"O{opportunity_number:05d}",
                account["account_id"],
                created_date.date(),
                expected_close_date.date(),
                stage,
                amount,
                days_open,
                rng.choice(
                    ["New Business", "Upsell", "Renewal"],
                    p=[0.35, 0.30, 0.35],
                ),
            ]
        )
        opportunity_number += 1

opportunities = pd.DataFrame(
    opportunity_rows,
    columns=[
        "opportunity_id",
        "account_id",
        "created_date",
        "expected_close_date",
        "stage",
        "opportunity_amount",
        "days_open",
        "opportunity_type",
    ],
)
opportunities.to_csv(RAW / "opportunities.csv", index=False)

activity_rows = []
activity_number = 1

for _, opportunity in opportunities.iterrows():
    activity_count = int(rng.integers(1, 8))
    start_date = pd.Timestamp(opportunity["created_date"])

    for _ in range(activity_count):
        activity_rows.append(
            [
                f"S{activity_number:06d}",
                opportunity["opportunity_id"],
                opportunity["account_id"],
                (
                    start_date
                    + pd.Timedelta(
                        days=int(
                            rng.integers(
                                0,
                                max(1, opportunity["days_open"]),
                            )
                        )
                    )
                ).date(),
                rng.choice(
                    [
                        "Email",
                        "Call",
                        "Meeting",
                        "Demo",
                        "Executive Review",
                    ]
                ),
                int(rng.integers(5, 75)),
            ]
        )
        activity_number += 1

activities = pd.DataFrame(
    activity_rows,
    columns=[
        "activity_id",
        "opportunity_id",
        "account_id",
        "activity_date",
        "activity_type",
        "duration_minutes",
    ],
)
activities.to_csv(RAW / "sales_activities.csv", index=False)

print("Synthetic commercial dataset created.")
print(f"Accounts: {len(accounts):,}")
print(f"Monthly performance rows: {len(performance):,}")
print(f"Opportunities: {len(opportunities):,}")
print(f"Sales activities: {len(activities):,}")
