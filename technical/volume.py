"""Volume analysis utilities."""

import pandas as pd


def volume_moving_average(df: pd.DataFrame, volume_col: str = "Volume", window: int = 20) -> pd.Series:
    """Return the moving average of volume."""
    return df[volume_col].rolling(window=window).mean()


def usdt_dominance(
    df: pd.DataFrame,
    usdt_volume_col: str = "USDT_Volume",
    total_volume_col: str = "Volume",
) -> pd.Series:
    """Return the USDT dominance (USDT volume / total volume)."""
    return df[usdt_volume_col] / df[total_volume_col]
