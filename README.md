# Commercial Revenue Intelligence Platform

## Overview
This project simulates an end-to-end commercial analytics environment for a global AdTech / SaaS company.

The goal is not to build a static dashboard. The goal is to convert raw CRM, revenue, campaign, and pipeline data into decisions about growth, account priorities, and commercial risk.

## Core Business Questions
- Where is revenue coming from?
- Which accounts, regions, and industries are growing or declining?
- How concentrated is revenue across key clients?
- Where is the sales pipeline getting stuck?
- Which opportunities and accounts deserve attention first?
- What commercial actions should leadership take?

## Tech Stack
- SQL
- Python / pandas
- Power BI or Tableau
- Jupyter Notebook

## Data Model
The synthetic dataset contains:
- account master data
- monthly campaign and revenue performance
- CRM opportunities
- sales activities

All data is synthetic and safe to publish publicly.

## Project Roadmap

### Phase 1 — SQL & Data Modeling
Build clean KPI logic and answer foundational revenue and pipeline questions.

### Phase 2 — Python Analytics
Add account segmentation, growth diagnostics, volatility analysis, Pareto analysis, and commercial prioritization.

### Phase 3 — BI Dashboard
Build three executive-facing views:
1. Executive Overview
2. Account & Segment Growth
3. Pipeline & Commercial Actions

### Phase 4 — Executive Recommendations
Translate analysis into concrete growth opportunities, revenue risks, account priorities, and pipeline actions.

## Repository Structure
```text
Commercial-Revenue-Intelligence-Platform/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── data_dictionary.md
│   └── project_plan.md
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
├── sql/
│   ├── 01_data_quality_checks.sql
│   ├── 02_revenue_kpis.sql
│   ├── 03_account_growth.sql
│   └── 04_pipeline_conversion.sql
├── src/
│   └── generate_synthetic_data.py
├── images/
├── .gitignore
├── requirements.txt
└── README.md
```

## What This Project Demonstrates
- Commercial problem framing
- SQL analytics
- Data modeling
- Revenue and account analysis
- Pipeline analytics
- Python-based business analysis
- BI storytelling
- Executive recommendation skills

## Current Sprint
**Question 1:** What is the monthly revenue trend from January 2024 to December 2025, and which months experienced the largest month-over-month increase and decrease?

The first goal is to solve this question in SQL, validate the logic, and explain the business meaning.

## Future Extensions
This repository is designed to evolve into:
- marketing incrementality analysis
- account renewal / expansion prediction
- AI commercial decision support
