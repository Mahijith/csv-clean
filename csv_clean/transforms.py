import re
import pandas as pd

def normalize_headers(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        re.sub(r'\s+', '_', c.strip().lower())
        for c in df.columns
    ]
    return df

def strip_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda c: c.str.strip())
    return df

def drop_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(how="all").reset_index(drop=True)