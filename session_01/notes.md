# Session 01 — Data Exploration & SQL Fundamentals

## 1. What I learned

In this session, I investigated suspicious order totals for the fictional e-commerce company Northstar Commerce.

The main workplace lesson was that I should not immediately change unusual data. I should:

1. Understand the dataset.
2. Identify suspicious records.
3. Verify them with calculations.
4. Confirm the finding.
5. Explain the result in business language.

I used Python/pandas for data inspection and validation, and SQLite/SQL for querying the same order data.

---

## 2. Important problem-solving logic

### Unusual does not mean incorrect

A high order total is not automatically an error.

For example:

- quantity = 1
- unit_price = 500
- total_amount = 500

This is high, but mathematically correct.

The important check was:

expected_total = quantity × unit_price

Then compare:

expected_total vs total_amount

### Confirmed issue

Order `ORD1030` had:

- quantity = 5
- unit_price = 16
- recorded total_amount = 800
- expected_total = 80

Therefore:

5 × 16 = 80

The recorded value of 800 does not match the expected value.

I confirmed one mismatched order in the dataset.

### Do not assume the cause

I can prove that the value is inconsistent, but I cannot prove why it became 800 without more evidence.

Possible causes should be investigated rather than assumed.

---

## 3. Data/system flow

The workflow used in this session was:

Raw CSV
→ Python inspection
→ understand rows, columns, and data types
→ filter suspicious records
→ calculate expected totals
→ compare expected and recorded values
→ verify the mismatch
→ load data into SQLite
→ explore with SQL
→ explain findings to the manager

Python and SQL were solving the same business problem in different ways.

---

## 4. Important Python syntax

### Import pandas

```python
import pandas as pd