-- 04_pipeline_conversion.sql

-- Pipeline value by stage
SELECT
    stage,
    COUNT(*) AS opportunity_count,
    ROUND(SUM(opportunity_amount), 2) AS pipeline_value,
    ROUND(AVG(days_open), 1) AS avg_days_open
FROM opportunities
GROUP BY stage
ORDER BY pipeline_value DESC;

-- Win rate by account tier
SELECT
    a.tier,
    COUNT(*) AS total_opportunities,
    SUM(CASE WHEN o.stage = 'Closed Won' THEN 1 ELSE 0 END) AS won_opportunities,
    ROUND(
        SUM(CASE WHEN o.stage = 'Closed Won' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS win_rate_pct
FROM opportunities o
JOIN accounts a
  ON o.account_id = a.account_id
GROUP BY a.tier
ORDER BY win_rate_pct DESC;

-- Stalled open opportunities
SELECT
    opportunity_id,
    account_id,
    stage,
    opportunity_amount,
    days_open
FROM opportunities
WHERE stage NOT IN ('Closed Won', 'Closed Lost')
  AND days_open > 60
ORDER BY opportunity_amount DESC;
