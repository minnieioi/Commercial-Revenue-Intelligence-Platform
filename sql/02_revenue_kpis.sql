-- 02_revenue_kpis.sql

-- Monthly revenue trend
SELECT
    month,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM monthly_performance
GROUP BY month
ORDER BY month;

-- Revenue by region
SELECT
    a.region,
    ROUND(SUM(p.revenue), 2) AS total_revenue
FROM monthly_performance p
JOIN accounts a
  ON p.account_id = a.account_id
GROUP BY a.region
ORDER BY total_revenue DESC;

-- Revenue by industry
SELECT
    a.industry,
    ROUND(SUM(p.revenue), 2) AS total_revenue
FROM monthly_performance p
JOIN accounts a
  ON p.account_id = a.account_id
GROUP BY a.industry
ORDER BY total_revenue DESC;

-- Top 10 accounts by revenue
SELECT
    a.account_name,
    a.region,
    a.industry,
    ROUND(SUM(p.revenue), 2) AS total_revenue
FROM monthly_performance p
JOIN accounts a
  ON p.account_id = a.account_id
GROUP BY a.account_name, a.region, a.industry
ORDER BY total_revenue DESC
LIMIT 10;
