# Lead Data Engineer Assessment

## Project Overview

This project implements a complete ETL pipeline using Databricks, PySpark, and Delta Lake.

## Architecture

Bronze
- customer_raw
- products_raw
- orders_raw

Silver
- customer_enriched
- product_enriched
- order_master

Gold
- profit_by_year
- profit_by_category
- profit_by_customer

## Technologies

- Python
- PySpark
- Databricks
- Delta Lake
- SQL
- Git
- GitHub

## Project Structure

data/
notebooks/
src/
tests/
docs/

## How to Run

1. Upload input files to DBFS.
2. Open `notebooks/run_pipeline.py`.
3. Run all notebooks.
4. Query the generated Delta tables.
