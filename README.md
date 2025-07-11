# ai-bot

This repository contains simple utilities for algorithmic trading experiments.

## Scoring Module

`scoring.py` provides functions that combine multiple trading indicators into a
confidence score. It also detects potential trend reversals based on score
changes and produces alert messages.

Example usage:

```python
from scoring import evaluate

indicators = {"rsi": 0.7, "macd": -0.2}
score, alert, reversal = evaluate("BTC", "1h", indicators)
print(alert)
```

