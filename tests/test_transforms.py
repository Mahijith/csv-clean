import pandas as pd
import pytest
from csv_clean.transforms import (
    normalize_headers,
    strip_whitespace,
    drop_empty_rows,
)

# --- normalize_headers ---

def test_normalize_headers_lowercases():
    df = pd.DataFrame(columns=["First Name", "Last Name"])
    result = normalize_headers(df)
    assert list(result.columns) == ["first_name", "last_name"]

def test_normalize_headers_strips_spaces():
    df = pd.DataFrame(columns=["  Email  ", " Phone"])
    result = normalize_headers(df)
    assert list(result.columns) == ["email", "phone"]

def test_normalize_headers_replaces_spaces_with_underscore():
    df = pd.DataFrame(columns=["Date Of Birth"])
    result = normalize_headers(df)
    assert list(result.columns) == ["date_of_birth"]

# --- strip_whitespace ---

def test_strip_whitespace_removes_leading_trailing():
    df = pd.DataFrame({"name": ["  Alice  ", " Bob"], "age": [25, 30]})
    result = strip_whitespace(df)
    assert list(result["name"]) == ["Alice", "Bob"]

def test_strip_whitespace_leaves_numbers_alone():
    df = pd.DataFrame({"name": ["Alice"], "age": [25]})
    result = strip_whitespace(df)
    assert list(result["age"]) == [25]

# --- drop_empty_rows ---

def test_drop_empty_rows_removes_all_nan_rows():
    df = pd.DataFrame({
        "name": ["Alice", None, "Bob"],
        "email": ["a@a.com", None, "b@b.com"]
    })
    result = drop_empty_rows(df)
    assert len(result) == 2

def test_drop_empty_rows_keeps_partial_rows():
    df = pd.DataFrame({
        "name": ["Alice", None],
        "email": ["a@a.com", "b@b.com"]
    })
    result = drop_empty_rows(df)
    assert len(result) == 2  # partial row kept — only ALL empty rows dropped