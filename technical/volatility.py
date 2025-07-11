"""Volatility measurement utilities."""

import pandas as pd


def atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    """Calculate the Average True Range (ATR)."""
    high = df["High"]
    low = df["Low"]
    close = df["Close"]

    prev_close = close.shift(1)

    tr = pd.concat(
        [
            (high - low).abs(),
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)

    return tr.rolling(period).mean()


def rolling_std(df: pd.DataFrame, price_col: str = "Close", window: int = 20) -> pd.Series:
    """Calculate rolling standard deviation."""
    return df[price_col].rolling(window=window).std()
