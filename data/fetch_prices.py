"""Utilities to fetch cryptocurrency prices from Binance."""

from __future__ import annotations

import requests
import pandas as pd
from typing import List, Dict


BASE_URL = "https://www.binance.com/api/v3"


def get_top_symbols(limit: int = 300, quote: str = "USDT") -> List[str]:
    """Return a list of the most traded symbols with the given quote asset.

    Parameters
    ----------
    limit : int
        Number of symbols to return sorted by quote volume.
    quote : str
        Quote asset to filter symbols, e.g. ``"USDT"``.

    Returns
    -------
    List[str]
        Symbol tickers like ``"BTCUSDT"``.
    """
    url = f"{BASE_URL}/ticker/24hr"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    symbols = [
        item
        for item in data
        if item["symbol"].endswith(quote)
        and not item["symbol"].endswith("UP" + quote)
        and not item["symbol"].endswith("DOWN" + quote)
    ]
    symbols.sort(key=lambda x: float(x.get("quoteVolume", 0)), reverse=True)
    return [item["symbol"] for item in symbols[:limit]]


def fetch_klines(symbol: str, interval: str, limit: int = 500) -> pd.DataFrame:
    """Fetch historical klines for a symbol and interval.

    Parameters
    ----------
    symbol : str
        Trading pair symbol such as ``"BTCUSDT"``.
    interval : str
        Binance interval string like ``"5m"`` or ``"1d"``.
    limit : int, optional
        Maximum number of candles to retrieve (default 500).

    Returns
    -------
    pandas.DataFrame
        DataFrame containing OHLCV data.
    """
    url = f"{BASE_URL}/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    raw = response.json()

    cols = [
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_asset_volume",
        "number_of_trades",
        "taker_base_volume",
        "taker_quote_volume",
        "ignore",
    ]
    df = pd.DataFrame(raw, columns=cols)
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df["close_time"] = pd.to_datetime(df["close_time"], unit="ms")
    numeric_cols = [
        "open",
        "high",
        "low",
        "close",
        "volume",
        "quote_asset_volume",
        "taker_base_volume",
        "taker_quote_volume",
    ]
    df[numeric_cols] = df[numeric_cols].astype(float)
    df["number_of_trades"] = df["number_of_trades"].astype(int)
    return df


DEFAULT_INTERVALS = ["5m", "15m", "2h", "4h", "1d"]


def fetch_prices(symbols: List[str], intervals: List[str] | None = None, limit: int = 500) -> Dict[str, Dict[str, pd.DataFrame]]:
    """Fetch OHLC data for multiple symbols and intervals.

    Parameters
    ----------
    symbols : List[str]
        List of trading pair symbols.
    intervals : List[str], optional
        Intervals to fetch. If ``None`` uses :data:`DEFAULT_INTERVALS`.
    limit : int, optional
        Number of candles per request.

    Returns
    -------
    Dict[str, Dict[str, pandas.DataFrame]]
        Mapping from symbol -> interval -> dataframe.
    """
    if intervals is None:
        intervals = DEFAULT_INTERVALS
    result: Dict[str, Dict[str, pd.DataFrame]] = {}
    for sym in symbols:
        result[sym] = {}
        for iv in intervals:
            try:
                result[sym][iv] = fetch_klines(sym, iv, limit=limit)
            except Exception as exc:  # pragma: no cover - simple error handling
                result[sym][iv] = pd.DataFrame()
    return result
