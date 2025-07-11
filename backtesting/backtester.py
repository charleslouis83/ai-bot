import pandas as pd
from .metrics import (
    cumulative_returns,
    annual_return,
    annual_volatility,
    sharpe_ratio,
    max_drawdown,
)


def run_backtest(data: pd.DataFrame, strategy_fn, **strategy_kwargs) -> dict:
    """Run a backtest using a strategy function.

    Parameters
    ----------
    data : DataFrame
        Price data with a 'Close' column.
    strategy_fn : callable
        Function that accepts ``data`` and returns a Series of signals (1 or 0).
    strategy_kwargs : dict
        Additional keyword arguments passed to ``strategy_fn``.
    Returns
    -------
    dict
        Performance metrics of the strategy.
    """
    signals = strategy_fn(data, **strategy_kwargs)
    returns = data['Close'].pct_change().fillna(0)
    strat_returns = signals.shift(1).fillna(0) * returns

    metrics = {
        'cumulative_return': cumulative_returns(strat_returns).iloc[-1],
        'annual_return': annual_return(strat_returns),
        'annual_volatility': annual_volatility(strat_returns),
        'sharpe_ratio': sharpe_ratio(strat_returns),
        'max_drawdown': max_drawdown(strat_returns),
    }
    return metrics
