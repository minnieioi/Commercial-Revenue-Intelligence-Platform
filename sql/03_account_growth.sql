-- 03_account_growth.sql
-- Adjust date syntax if needed for your SQL engine.

WITH monthly_account_revenue AS (
    SELECT
        account_id,
        month,
        SUM(revenue) AS revenue
    FROM monthly_performance
    GROUP BY account_id, month
),
with_previous AS (
    SELECT
        account_id,
        month,
        revenue,
        LAG(revenue) OVER (
            PARTITION BY account_id
            ORDER BY month
        ) AS previous_month_revenue
    FROM monthly_account_revenue
)
SELECT
    account_id,
    month,
    revenue,
    previous_month_revenue,
    ROUND(
        (revenue - previous_month_revenue) * 100.0
        / NULLIF(previous_month_revenue, 0),
        2
    ) AS mom_growth_pct
FROM with_previous
ORDER BY account_id, month;
