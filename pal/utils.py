import numpy as np
import pandas as pd

from .params import Params


def load_ffme_returns(cols=None):
    """
    Load the Fama-French Dataset for the returns of the Top and Bottom Deciles by MarketCap
    """
    if cols is None:
        cols = ["Lo 10", "Hi 10"]
    df = pd.read_csv(Params.DATA_FFME_PATH, index_col=0, na_values=-99.99)
    df.index = pd.to_datetime(df.index, format="%Y%m").to_period("M")
    df /= 100
    df = df[cols]
    df.rename({"Lo 10": "smallCap", "Hi 10": "largeCap"}, axis=1, inplace=True)
    return df


def load_hfi_returns():
    """
    Load and format the EDHEC Hedge Fund Index Returns
    """
    df = pd.read_csv(Params.DATA_HFI_PATH, index_col=0)
    df.index = pd.to_datetime(df.index).to_period("M")
    df /= 100
    return df


def dict_to_keys_values(dic):
    keys, values = list(dic.keys()), list(dic.values())
    return keys, values


def numpy_assert_almost_dicts(dict1, dict2):
    keys1, values1 = dict_to_keys_values(dict1)
    keys2, values2 = dict_to_keys_values(dict2)
    return np.testing.assert_equal(keys1, keys2), np.testing.assert_almost_equal(values1, values2)
