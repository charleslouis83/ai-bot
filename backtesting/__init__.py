"""Backtesting package for running historical simulations."""

from .data import load_price_data
from .indicators import moving_average, crossover_strategy
from .backtester import run_backtest
from . import metrics

__all__ = [
    'load_price_data',
    'moving_average',
    'crossover_strategy',
    'run_backtest',
    'metrics',
]
