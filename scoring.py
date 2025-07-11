"""Scoring utilities for cryptocurrency trading bots."""

from typing import Dict, Optional, Tuple


def compute_confidence_score(indicators: Dict[str, float],
                             weights: Optional[Dict[str, float]] = None) -> float:
    """Combine indicator values into a weighted average score."""
    if not indicators:
        return 0.0

    if weights is None:
        weights = {}

    total = 0.0
    weight_sum = 0.0
    for name, value in indicators.items():
        weight = weights.get(name, 1.0)
        total += value * weight
        weight_sum += weight
    return total / weight_sum if weight_sum else 0.0


def detect_trend_reversal(previous_score: float, current_score: float,
                          threshold: float = 0.5) -> bool:
    """Return True if score change indicates a potential trend reversal."""
    change = current_score - previous_score
    if abs(change) >= threshold and (previous_score >= 0) != (current_score >= 0):
        return True
    return False


def generate_alert(coin: str, timeframe: str, score: float, reversal: bool) -> str:
    """Generate a human-readable alert message."""
    status = "Trend reversal" if reversal else "Score update"
    return f"[{coin} - {timeframe}] {status}: confidence score={score:.2f}"


def evaluate(coin: str, timeframe: str, indicators: Dict[str, float],
             previous_score: Optional[float] = None,
             weights: Optional[Dict[str, float]] = None,
             threshold: float = 0.5) -> Tuple[float, str, bool]:
    """Evaluate indicators and return the score, alert message and reversal flag."""
    current_score = compute_confidence_score(indicators, weights)
    reversal = False
    if previous_score is not None:
        reversal = detect_trend_reversal(previous_score, current_score, threshold)
    alert = generate_alert(coin, timeframe, current_score, reversal)
    return current_score, alert, reversal
