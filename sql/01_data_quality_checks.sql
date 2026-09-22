-- 01_data_quality_checks.sql
-- Run these checks before analysis.

-- Row counts
SELECT COUNT(*) AS account_rows FROM accounts;
SELECT COUNT(*) AS performance_rows FROM monthly_performance;
SELECT COUNT(*) AS opportunity_rows FROM opportunities;
SELECT COUNT(*) AS activity_rows FROM sales_activities;

-- Duplicate primary keys
SELECT account_id, COUNT(*)
FROM accounts
GROUP BY account_id
HAVING COUNT(*) > 1;

SELECT opportunity_id, COUNT(*)
FROM opportunities
GROUP BY opportunity_id
HAVING COUNT(*) > 1;

-- Null key checks
SELECT COUNT(*) AS null_account_ids
FROM monthly_performance
WHERE account_id IS NULL;

-- Orphan records
SELECT p.account_id
FROM monthly_performance p
LEFT JOIN accounts a
  ON p.account_id = a.account_id
WHERE a.account_id IS NULL;
