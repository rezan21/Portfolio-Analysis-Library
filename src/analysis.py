import pandas as pd


def analyse_returns(returns: pd.Series, freq: int) -> dict:
    periods = len(returns)
    total_gross = (returns + 1).prod()
    total_ret = (returns + 1).prod() - 1
    per_period_gross = total_gross ** (1 / periods)
    per_period_ret = per_period_gross - 1
    annual_gross = per_period_gross ** freq
    annual_ret = annual_gross - 1
    return {
        "periods": periods,
        "total_gross": total_gross,
        "total_ret": total_ret,
        "per_period_gross": per_period_gross,
        "per_period_ret": per_period_ret,
        "annual_gross": annual_gross,
        "annual_ret": annual_ret,
    }


def analyse_risk(returns: pd.Series, freq: int) -> dict:
    std = returns.std()
    semi_dev = returns[returns < 0].std(ddof=0)
    var = returns.var()
    annual_vol = std * (freq ** 0.5)
    return {
        "std": std,
        "semi_dev": semi_dev,
        "var": var,
        "annual_vol": annual_vol,
    }


def calculate_annual_sharpe(annual_ret, annual_vol, risk_free_rate):
    return (annual_ret - risk_free_rate) / annual_vol


def simulate_wealth_index(returns, A):
    return A * (returns + 1).cumprod()


def get_prev_high(series: pd.Series):
    return series.cummax()


def get_prev_low(series: pd.Series):
    return series.cummin()


def calculate_max_drawdown(wealth_index, prev_high) -> dict:
    drawdown = (wealth_index - prev_high) / prev_high
    max_drawdown = drawdown.min()  # drawdown is negative
    id_max_drawdown = drawdown.idxmin()
    return {
        "wealth_index": wealth_index,
        "prev_high": prev_high,
        "drawdown": drawdown,
        "max_drawdown": max_drawdown,
        "id_max_drawdown": id_max_drawdown,
    }


def get_skewness(series: pd.Series):
    # normal skewness is 0
    num = ((series - series.mean()) ** 3).sum()
    denum = len(series) * series.std(ddof=0) ** 3
    return num / denum


def get_kurtosis(series: pd.Series, excess):
    # normal kurtosis is 3
    num = ((series - series.mean()) ** 4).sum()
    denum = len(series) * series.std(ddof=0) ** 4
    kurtosis = num / denum
    if excess:
        kurtosis -= 3
    return kurtosis


# def get_VaR_historic(r, var_pct: int = 95):
#     assert 1 <= var_pct <= 100
#     if isinstance(r, pd.DataFrame):
#         return r.aggregate(get_VaR_historic, var_pct=var_pct)
#     elif isinstance(r, pd.Series):
#         return -np.percentile(r, (100 - var_pct))
#     else:
#         raise TypeError("Expected DataFrame or Series")
