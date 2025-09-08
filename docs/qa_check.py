#!/usr/bin/env python
import json, pandas as pd, sys, os

df = pd.read_csv("data/lexicon.csv", dtype=str, encoding="utf-8").fillna("")
allowed = {"positive","negative","uncertain","litigious","constraining","superfluous","stopword"}

errors = []

# Column presence
required_cols = ["term","label","category","source","added_in_version","deprecated","deprecated_in_version","alias_of","notes"]
missing = set(required_cols) - set(df.columns)
if missing:
    errors.append(f"Missing columns: {sorted(list(missing))}")

# Label values
bad = df.loc[~df["label"].isin(allowed)]
if len(bad):
    errors.append(f"Found {len(bad)} rows with invalid labels (allowed: {sorted(list(allowed))}).")

# Duplicates
dups = df.duplicated(subset=["term","label"], keep=False)
if dups.any():
    dup_rows = df.loc[dups, ["term","label"]]
    errors.append(f"Duplicate term+label pairs:\n{dup_rows.to_string(index=False)}")

# Encoding check (rudimentary): ensure file can be read in UTF-8 – already satisfied if we got here

if errors:
    print("QA FAILED\n" + "\n\n".join(errors))
    sys.exit(1)
else:
    print("QA PASSED: schema, labels, duplicates OK")
