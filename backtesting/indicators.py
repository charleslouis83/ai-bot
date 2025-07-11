import pandas as pd


def moving_average(series: pd.Series, window: int) -> pd.Series:
    """Simple moving average."""
    return series.rolling(window).mean()


def crossover_strategy(df: pd.DataFrame, short_window: int = 50, long_window: int = 200) -> pd.Series:
    """Generate trading signals based on moving average crossover.

    Returns a Series of 1 (long) or 0 (flat) signals.
    """
    short_ma = moving_average(df['Close'], short_window)
    long_ma = moving_average(df['Close'], long_window)
    signals = (short_ma > long_ma).astype(int)
    return signals
