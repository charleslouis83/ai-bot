# ai-bot

This repository provides utilities for technical analysis. The `technical`
package includes modules for common analytics such as volume analysis, USDT
 dominance, volatility measurements, and support/resistance identification.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Example of computing ATR and support levels:

```python
import pandas as pd
from technical import atr, find_support_resistance

# DataFrame ``df`` must contain ``High``, ``Low`` and ``Close`` columns
atr_series = atr(df)
supports, resistances = find_support_resistance(df)
```
