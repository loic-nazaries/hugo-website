---
title: "Data Pipeline Best Practices: From Raw Data to Clean Output"
date: 2026-04-26T10:00:00+01:00
image: "images/portfolio/data_pipeline.png"
tags: ["data engineering", "python", "ETL", "BigQuery"]
description: "Key principles for building reliable, maintainable data pipelines — covering extraction, transformation, loading, and the tools that make it repeatable."
draft: false
---

A data pipeline moves data from one or more sources through a series of transformations to a destination where it can be analysed or served. Getting this right from the start saves enormous debugging effort later.

## The ETL Pattern

Most pipelines follow the Extract → Transform → Load (ETL) pattern:

1. **Extract** — pull data from source systems (databases, APIs, files)
2. **Transform** — clean, validate, reshape, and enrich the data
3. **Load** — write the result to a destination (data warehouse, dashboard, file)

A variation, ELT, loads raw data first and transforms it inside the destination (common with cloud data warehouses like BigQuery).

## Principle 1: Separate Concerns

Keep extraction, transformation, and loading in separate functions or modules. This makes each stage independently testable and replaceable.

```python
def extract(source_path: str) -> pd.DataFrame:
    return pd.read_csv(source_path)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["date", "value"])
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = df["value"].clip(lower=0)
    return df

def load(df: pd.DataFrame, dest_path: str) -> None:
    df.to_parquet(dest_path, index=False)
```

## Principle 2: Validate Early

Catch bad data at the extraction stage before it corrupts your transforms.

```python
def validate(df: pd.DataFrame) -> None:
    assert "date" in df.columns, "Missing 'date' column"
    assert df["value"].dtype in ["float64", "int64"], "Value column must be numeric"
    assert not df.duplicated(subset=["date", "site_id"]).any(), "Duplicate records found"
```

Consider libraries like [Pandera](https://pandera.readthedocs.io/) or [Great Expectations](https://greatexpectations.io/) for schema-level validation.

## Principle 3: Make Pipelines Idempotent

Running the pipeline twice should produce the same result as running it once. Use upsert logic or partition-based writes rather than appending blindly.

## Principle 4: Log Everything

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

logger = logging.getLogger(__name__)
logger.info("Extracted %d rows from %s", len(df), source_path)
```

Log row counts at each stage so you can detect where data is being dropped unexpectedly.

## Principle 5: Parameterise, Don't Hardcode

Use configuration files or environment variables for paths, credentials, and dates. Never hardcode a connection string or file path inside a function.

```python
import os
DB_URL = os.environ["DATABASE_URL"]
```

## Cloud Pipelines: BigQuery Example

For large datasets, a cloud data warehouse removes the need to manage local storage. The ETL process for BigQuery and Data Studio is demonstrated in the [Google BigQuery & Data Studio portfolio project](/en/portfolio/google_bigquery_datastudio), including a reusable Python script published as a GitHub Gist.

## Summary

| Practice | Why it matters |
|---|---|
| Separate ETL stages | Independent testing and reuse |
| Validate at extraction | Catch bad data early |
| Idempotent writes | Safe to re-run after failures |
| Log row counts at each stage | Detect silent data loss |
| Parameterise configuration | Portability across environments |

Consistent application of these principles is what separates a script that ran once from a pipeline that runs reliably in production.
