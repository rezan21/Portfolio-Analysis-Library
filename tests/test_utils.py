import numpy as np
import pandas as pd
import pytest
from pal import utils


def test_load_ffme_returns():
    df = utils.load_ffme_returns()
    assert df.shape == (1110, 2)
    assert df.index[0] == pd.Period("1926-07")
    assert df.index[-1] == pd.Period("2018-12")
    assert df.columns.tolist() == ["smallCap", "largeCap"]


def test_load_hfi_returns():
    df = utils.load_hfi_returns()
    assert df.shape == (263, 13)
    assert df.index[0] == pd.Period("1997-01")
    assert df.index[-1] == pd.Period("2018-11")


def test_dict_to_keys_values():
    d = {"a": 1, "b": 2, "c": 3, "d": None}
    keys, values = utils.dict_to_keys_values(d)
    assert keys == ["a", "b", "c", "d"]
    assert values == [1, 2, 3, None]


def test_numpy_assert_almost_dicts():
    dict1 = {"b": np.array([1, 2, 0.2])}
    dict2 = {"b": np.array([1, 2, 3 * 0.1 - 0.1])}  # almost same
    dict3 = {"b": np.array([999, 888, 444])}  # completely different

    # no exception expected
    utils.numpy_assert_almost_dicts(dict1, dict2)

    # assert for expected failure
    with pytest.raises(AssertionError):
        utils.numpy_assert_almost_dicts(dict1, dict3)
