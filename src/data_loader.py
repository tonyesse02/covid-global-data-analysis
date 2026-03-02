from __future__ import annotations

import pandas as pd
from .config import OWID_URL


def load_owid_data(url: str = OWID_URL) -> pd.DataFrame:
    """
    Download and load OWID COVID-19 dataset.
    Converts 'date' to datetime when available.
    """
    df = pd.read_csv(url)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df
