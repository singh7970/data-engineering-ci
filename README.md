DATA ENGINEERING CI PROJECT
Overview

This project demonstrates a production-style Data Engineering CI (Continuous Integration) pipeline using Python, SQL concepts, Pytest, and GitHub Actions.

Every code change automatically triggers data quality tests to ensure the data pipeline remains reliable and production-safe.

Problem Statement

In real-world data systems, broken pipelines or bad data can silently corrupt analytics and business decisions.

This project solves that problem by:

Validating raw data

Enforcing schema and data quality rules

Automatically testing pipelines on every code change

Architecture

Raw CSV Data
→ Extract (Python)
→ Transform (Python / SQL)
→ Load (CSV output)
→ Data Quality Tests
→ CI Pipeline (GitHub Actions)

If any step fails, the pipeline is blocked.

Project Structure

data-engineering-ci/

data/

sales.csv

scripts/

extract.py

transform.py

load.py

tests/

test_data_quality.py

sql/

transform.sql

requirements.txt

conftest.py

.github/workflows/ci.yml

Key Technologies

Python 3.12

Pandas

Pytest

SQL

GitHub Actions (CI)

Data Quality Checks

The pipeline validates:

Required columns exist

Primary keys are not null

Data types and formats are correct

Failures are detected early during CI execution.

CI Workflow

Developer pushes code to GitHub

GitHub Actions creates a clean Linux environment

Dependencies are installed

Data quality tests are executed

Pipeline passes or fails automatically

This prevents broken pipelines from reaching production.

How to Run Locally

Create virtual environment

Install dependencies

Run tests

Commands:
source env/bin/activate
pip install -r requirements.txt
python -m pytest tests/

Why This Project Matters

This project demonstrates real-world data engineering skills:

CI/CD for data pipelines

Data quality validation

Debugging production-like failures

Environment and dependency management

Interview Summary

"I built a data engineering pipeline with automated CI using GitHub Actions. Every data pipeline change triggers data quality tests, preventing broken data from reaching production."

END OF README
