import numpy as np
from pal import portfolio, utils

from .desired import Desired

ffme = utils.load_ffme_returns()
hfi = utils.load_hfi_returns()


def test_analyse_returns_annual_ret():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_ANN_RET
    actual = ffme_portfolio.analysed_returns["annual_ret"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_analyse_returns_per_period_ret():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_PER_PERIOD_RET
    actual = ffme_portfolio.analysed_returns["per_period_ret"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_analyse_risk_annual_vol():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_ANN_VOL
    actual = ffme_portfolio.analysed_risk["annual_vol"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_analyse_risk_semi_dev():
    hfi_portfolio = portfolio.Portfolio(hfi, 12)
    desired = Desired.HFI_SEMI_DEV
    actual = hfi_portfolio.analysed_risk["semi_dev"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_calculate_annual_sharpe_explicit():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_ANN_SHARPE
    _ = ffme_portfolio.analysed_returns
    _ = ffme_portfolio.analysed_risk
    ffme_portfolio.get_annual_sharpe()
    actual = ffme_portfolio.annual_sharpe.to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_calculate_annual_sharpe_implicit():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_ANN_SHARPE
    ffme_portfolio.get_annual_sharpe()
    actual = ffme_portfolio.annual_sharpe.to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_calculate_annual_sharpe_3pct_implicit():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_ANN_SHARPE_3PCT
    ffme_portfolio.get_annual_sharpe(0.03)
    actual = ffme_portfolio.annual_sharpe.to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_simulate_wealth_index():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_WEALTH_INDEX
    ffme_portfolio.get_wealth_index(1000)
    actual = ffme_portfolio.wealth_index["largeCap"].tolist()[:5]
    np.testing.assert_almost_equal(desired, actual)


def test_calculate_max_drawdown_explicit():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_MAX_DRAWDOWN
    ffme_portfolio.get_prev_high(ffme_portfolio.get_wealth_index(1000))
    ffme_portfolio.get_max_drawdown(A=1000)
    actual = ffme_portfolio.drawdown["max_drawdown"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_calculate_max_drawdown_implicit():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_MAX_DRAWDOWN
    ffme_portfolio.get_max_drawdown(A=1000)
    actual = ffme_portfolio.drawdown["max_drawdown"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_calculate_max_drawdown_index():
    ffme_portfolio = portfolio.Portfolio(ffme, 12)
    desired = Desired.FFME_MAX_DRAWDOWN_PERIOD  # aka index
    ffme_portfolio.get_max_drawdown(A=1000)
    actual = ffme_portfolio.drawdown["id_max_drawdown"].to_dict()
    np.testing.assert_equal(actual, desired)


def test_get_skewness():
    hfi_portfolio = portfolio.Portfolio(hfi, 12)
    desired = Desired.HFI_SKEWNESS
    hfi_portfolio.get_skewness()
    actual = hfi_portfolio.skewness.sort_values().to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_get_kurtosis():
    hfi_portfolio = portfolio.Portfolio(hfi, 12)
    desired = Desired.HFI_KURTOSIS
    hfi_portfolio.get_kurtosis(excess=False)
    actual = hfi_portfolio.kurtosis.to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)
