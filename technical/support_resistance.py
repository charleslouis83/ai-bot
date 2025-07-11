"""Support and resistance identification."""

import pandas as pd


def find_support_resistance(df: pd.DataFrame, price_col: str = "Close", window: int = 5):
    """Identify support and resistance points using rolling minima and maxima."""
    span = window * 2 + 1
    local_min = df[price_col] == df[price_col].rolling(span, center=True).min()
    local_max = df[price_col] == df[price_col].rolling(span, center=True).max()

    supports = df[local_min][price_col]
    resistances = df[local_max][price_col]
    return supports, resistances
