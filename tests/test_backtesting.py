import pandas as pd
import numpy as np

from backtesting import crossover_strategy, run_backtest


def create_sample_data(days=300):
    rng = pd.date_range('2020-01-01', periods=days, freq='D')
    prices = 100 + np.cumsum(np.random.randn(days))
    df = pd.DataFrame({'Close': prices}, index=rng)
    return df


def test_backtest_runs():
    data = create_sample_data()
    metrics = run_backtest(data, crossover_strategy, short_window=5, long_window=20)
    assert 'cumulative_return' in metrics
    assert 'sharpe_ratio' in metrics
