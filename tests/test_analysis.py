import numpy as np
from pal import analysis, utils

from .desired import Desired

ffme = utils.load_ffme_returns()
hfi = utils.load_hfi_returns()


def test_analyse_returns_annual_ret():
    desired = Desired.FFME_ANN_RET
    actual = analysis.analyse_returns(ffme, 12)["annual_ret"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_analyse_returns_per_period_ret():
    desired = Desired.FFME_PER_PERIOD_RET
    actual = analysis.analyse_returns(ffme, 12)["per_period_ret"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_analyse_risk_annual_vol():
    desired = Desired.FFME_ANN_VOL
    actual = analysis.analyse_risk(ffme, 12)["annual_vol"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_analyse_risk_semi_dev():
    desired = Desired.HFI_SEMI_DEV
    actual = analysis.analyse_risk(hfi, 12)["semi_dev"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_calculate_annual_sharpe():
    desired = Desired.FFME_ANN_SHARPE
    annual_ret = analysis.analyse_returns(ffme, 12)["annual_ret"]
    annual_vol = analysis.analyse_risk(ffme, 12)["annual_vol"]
    risk_free_rate = 0.0
    actual = analysis.calculate_annual_sharpe(
        annual_ret=annual_ret, annual_vol=annual_vol, risk_free_rate=risk_free_rate
    ).to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_calculate_annual_sharpe_3pct():
    desired = Desired.FFME_ANN_SHARPE_3PCT
    annual_ret = analysis.analyse_returns(ffme, 12)["annual_ret"]
    annual_vol = analysis.analyse_risk(ffme, 12)["annual_vol"]
    risk_free_rate = 0.03
    actual = analysis.calculate_annual_sharpe(
        annual_ret=annual_ret, annual_vol=annual_vol, risk_free_rate=risk_free_rate
    ).to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_simulate_wealth_index():
    desired = Desired.FFME_WEALTH_INDEX
    actual = analysis.simulate_wealth_index(ffme, 1000)["largeCap"].tolist()[:5]
    np.testing.assert_almost_equal(desired, actual)


def test_calculate_max_drawdown():
    desired = Desired.FFME_MAX_DRAWDOWN
    wealth_index = analysis.simulate_wealth_index(ffme, 1000)
    prev_high = analysis.get_prev_high(wealth_index)
    actual = analysis.calculate_max_drawdown(wealth_index=wealth_index, prev_high=prev_high)["max_drawdown"].to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_calculate_max_drawdown_index():
    desired = Desired.FFME_MAX_DRAWDOWN_PERIOD  # aka index
    wealth_index = analysis.simulate_wealth_index(ffme, 1000)
    prev_high = analysis.get_prev_high(wealth_index)
    actual = analysis.calculate_max_drawdown(wealth_index=wealth_index, prev_high=prev_high)[
        "id_max_drawdown"
    ].to_dict()
    np.testing.assert_equal(actual, desired)


def test_get_skewness():
    desired = Desired.HFI_SKEWNESS
    actual = analysis.get_skewness(hfi).sort_values().to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)


def test_get_kurtosis():
    desired = Desired.HFI_KURTOSIS
    actual = analysis.get_kurtosis(hfi, excess=False).to_dict()
    utils.numpy_assert_almost_dicts(desired, actual)
