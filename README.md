# Portfolio-Analysis-Library (PAL)

## WORK IN PROGRESS (WIP)

## Usage:
```
pip install portfolio-analysis-library
```

in python:
```
import pal
import pandas as pd

portfolio = pal.Portfolio(pd.Series([0.2, 0.3, -0.1, 0.2, -0.5]), 12)
portfolio.get_annual_sharpe(risk_free_rate=0.02)
print(portfolio.annual_sharpe)
```

## Development
```bash
pip install -r .[dev]
```
