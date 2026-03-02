from __future__ import annotations

from typing import Iterable, Optional
import pandas as pd


def filter_locations(df: pd.DataFrame, locations: Iterable[str]) -> pd.DataFrame:
    if "location" not in df.columns:
        raise ValueError("Column 'location' not found.")
    locations = list(locations)
    return df[df["location"].isin(locations)].copy()


def filter_year_range(df: pd.DataFrame, start_year: int, end_year: int, date_col: str = "date") -> pd.DataFrame:
    if date_col not in df.columns:
        raise ValueError(f"Column '{date_col}' not found.")
    out = df.copy()
    years = pd.to_datetime(out[date_col], errors="coerce").dt.year
    return out[(years >= start_year) & (years <= end_year)].copy()


def add_year(df: pd.DataFrame, date_col: str = "date") -> pd.DataFrame:
    if date_col not in df.columns:
        raise ValueError(f"Column '{date_col}' not found.")
    out = df.copy()
    out["year"] = pd.to_datetime(out[date_col], errors="coerce").dt.year
    return out


def yearly_agg(
    df: pd.DataFrame,
    value_col: str,
    agg: str = "sum",
    group_cols: Optional[list[str]] = None,
) -> pd.DataFrame:
    """
    Aggregate a metric by year (+ optional group columns).
    agg: "sum" | "max" | "mean"
    """
    group_cols = group_cols or []
    if "year" not in df.columns:
        df = add_year(df)

    cols = ["year"] + group_cols
    for c in cols:
        if c not in df.columns:
            raise ValueError(f"Column '{c}' not found.")
    if value_col not in df.columns:
        raise ValueError(f"Column '{value_col}' not found.")

    gb = df.groupby(cols, dropna=False)[value_col]
    if agg == "sum":
        out = gb.sum(min_count=1)
    elif agg == "max":
        out = gb.max()
    elif agg == "mean":
        out = gb.mean()
    else:
        raise ValueError("agg must be one of: 'sum', 'max', 'mean'")

    return out.reset_index().sort_values(cols)
