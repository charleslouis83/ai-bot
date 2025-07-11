import pandas as pd


def load_price_data(filepath: str) -> pd.DataFrame:
    """Load OHLCV price data from a CSV file.

    The CSV should contain columns like 'Open', 'High', 'Low', 'Close', 'Volume'.
    The function parses dates and sets the index to the first column.
    """
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    return df
