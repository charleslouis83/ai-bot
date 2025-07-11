import pandas as pd
import numpy as np


def cumulative_returns(returns: pd.Series) -> pd.Series:
    """Compute cumulative returns from periodic returns."""
    return (1 + returns).cumprod() - 1


def annual_return(returns: pd.Series, periods_per_year: int = 252) -> float:
    compounded = (1 + returns).prod()
    years = len(returns) / periods_per_year
    return compounded ** (1 / years) - 1 if years > 0 else np.nan


def annual_volatility(returns: pd.Series, periods_per_year: int = 252) -> float:
    return returns.std() * np.sqrt(periods_per_year)


def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0, periods_per_year: int = 252) -> float:
    excess = returns - risk_free_rate / periods_per_year
    vol = returns.std()
    return np.nan if vol == 0 else (excess.mean() / vol) * np.sqrt(periods_per_year)


def max_drawdown(returns: pd.Series) -> float:
    cum = cumulative_returns(returns) + 1
    peak = cum.cummax()
    drawdown = (cum - peak) / peak
    return drawdown.min()
