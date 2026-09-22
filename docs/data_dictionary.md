# Data Dictionary

## accounts.csv
- `account_id`: Unique account identifier
- `account_name`: Synthetic client name
- `region`: North America / APAC / Europe
- `industry`: Gaming / E-commerce / Beauty / Consumer Apps / SaaS
- `tier`: Enterprise / Mid-Market / SMB
- `acquisition_channel`: Agency / Direct Sales / Partner Referral / Inbound
- `signup_date`: First customer relationship date
- `annual_contract_value`: Approximate annual contract value

## monthly_performance.csv
- `account_id`: Account key
- `month`: Month of activity
- `revenue`: Monthly revenue
- `ad_spend`: Monthly marketing/media spend
- `impressions`: Ad impressions
- `clicks`: Click volume
- `conversions`: Conversion volume
- `roas`: Revenue / ad spend
- `ctr`: Click-through rate
- `conversion_rate`: Conversions / clicks

## opportunities.csv
- `opportunity_id`: Unique opportunity identifier
- `account_id`: Account key
- `created_date`: Opportunity creation date
- `expected_close_date`: Expected close date
- `stage`: Pipeline stage
- `opportunity_amount`: Potential contract value
- `days_open`: Days opportunity has been open
- `opportunity_type`: New Business / Upsell / Renewal

## sales_activities.csv
- `activity_id`: Unique activity identifier
- `opportunity_id`: Opportunity key
- `account_id`: Account key
- `activity_date`: Activity date
- `activity_type`: Email / Call / Meeting / Demo / Executive Review
- `duration_minutes`: Activity duration
