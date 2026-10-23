# Bastien Deffradas

**Business Analyst in Hamburg · Process and operations improvement · Data as a tool**

I help operations and finance teams see where a process loses time or money, fix it, and show the gain with numbers. I work with Python, SQL, Excel, Power BI and SAP data.

## What I work on

- **Process improvement and automation** in industrial operations
- **Budget vs. actual analysis** and KPI reporting for controlling teams
- **Data pipelines** that check their input and can be re-run by someone else
- **Practical AI use cases**: choosing what is worth building, and measuring the value after go-live

Sectors I care about most: **aerospace, defence and maritime logistics**.

## Featured work

| Project | The problem | What I built |
|---|---|---|
| [AI Use-Case Pilot Kit](https://github.com/bastiendfd/ai-use-case-pilot-kit) | Companies collect many AI ideas but find it hard to choose which ones to fund, and often do not check later if they paid off. | A 5-step method: intake form, EU AI Act screening, score out of 100, business case in Excel and value tracking after go-live, worked through six fictional cases. |
| [OpsPilot AI](https://github.com/bastiendfd/opspilot-ai) | Finding out why actual costs differ from the budget can take controllers hours. | A local Python app that reads actual, budget and forecast Excel files, stops when the data has errors, finds the account and cost centre behind the largest budget gap, and lists the source rows behind it. Streamlit UI, tests, CI. |
| [ETL Pipeline Automation](https://github.com/bastiendfd/etl-pipeline-automation) | CSV files arrive with errors, and nobody knows which rows were dropped or why. | A command-line pipeline that checks every row, keeps the rejected rows with the reason, and writes an audit summary. |
| [KPI Report Generator](https://github.com/bastiendfd/kpi-report-generator) | Monthly KPI reports are often rebuilt by hand. | A command-line tool that turns a revenue and cost CSV into a Markdown KPI report, and stops with a clear error on bad input. |
| [Maintenance Work Order API](https://github.com/bastiendfd/maintenance-work-order-api) | Maintenance teams need one clear list of work orders and where each one stands. | A small Flask and SQLite REST API to create, list, update and delete work orders. It accepts only known status values and rejects incomplete requests. |
| [Turbofan Health ML](https://github.com/bastiendfd/turbofan-health-ml) | A remaining-life model looks better than it is if the same engine is in both the training and the test data. | A baseline model that keeps each engine on one side of the split, plus a reader for the NASA C-MAPSS file format. |
| [Retail BI and Forecasting Lab](https://github.com/bastiendfd/msc-bi-analytics-retail-forecasting) | Retail teams need to know which product groups earn the most and what sales to expect next. | A practice lab on my MSc Business Intelligence topics: margin by product group, a simple 7-day sales forecast and a local Flask dashboard. |

All featured projects use **fictional or public data only** and run locally. They are portfolio work, not production systems; each README lists its limits.

## Other projects

- [Predictive Maintenance ML](https://github.com/bastiendfd/predictive-maintenance-ml): a simple anomaly check on synthetic machine sensor data that shows which sensor raised each alert.
- [Cost Tracker CLI](https://github.com/bastiendfd/cost-tracker-cli): log and sum maintenance costs in SQLite from the command line.
- [Logistic Challenge](https://github.com/bastiendfd/LogisticChallenge): a small transport optimisation model (linear programming with PuLP).
- University and early learning exercises (algorithms, small tools, robotics) are archived but stay public as a record of how I learned.

## Principles

- No employer, customer or personal data in public repositories.
- No passwords, tokens or keys in code.
- Tests and clear limits matter as much as features.
- Simple methods first; AI only where it clearly helps, and a person makes the decision.

## Tools

`Python` · `SQL` · `pandas` · `Excel` · `Power BI` · `SAP` · `SQLite` · `Flask` · `Streamlit` · `Git` · `GitHub Actions` · `Docker`

---

Based in Hamburg, Germany. Open to process, operations and transformation roles.
