import pandas as pd

import pal.analysis as analysis


class Portfolio:
    def __init__(self, returns: pd.Series, freq: int):
        """given returns, perform analysis

        Args:
            returns (Series-like): net returns in terms of percentage. e.g: 50% = 0.5
            freq (int): frequency the data is representing. e.g: 252 = daily, 12 = monthly, 52 = weekly
        """
        self.returns = returns
        self.freq = freq

        self.__analysed_returns = None
        self.__analysed_risk = None
        self.annual_sharpe = None
        self.wealth_index = None
        self.prev_high = None
        self.prev_low = None
        self.drawdown = None
        self.skewness = None
        self.kurtosis = None

    @property
    def analysed_returns(self):
        self.__analysed_returns = analysis.analyse_returns(returns=self.returns, freq=self.freq)
        return self.__analysed_returns

    @property
    def analysed_risk(self):
        self.__analysed_risk = analysis.analyse_risk(returns=self.returns, freq=self.freq)
        return self.__analysed_risk

    def get_annual_sharpe(self, risk_free_rate: float = 0):
        if not all([self.__analysed_returns, self.__analysed_risk]):
            _ = self.analysed_returns
            _ = self.analysed_risk
        self.annual_sharpe = analysis.calculate_annual_sharpe(
            annual_ret=self.__analysed_returns["annual_ret"],
            annual_vol=self.__analysed_risk["annual_vol"],
            risk_free_rate=risk_free_rate,
        )
        return self.annual_sharpe

    def get_wealth_index(self, A=1000):
        self.wealth_index = analysis.simulate_wealth_index(returns=self.returns, A=A)
        return self.wealth_index

    def get_prev_high(self, series: pd.Series):
        self.prev_high = analysis.get_prev_high(series=series)
        return self.prev_high

    def get_prev_low(self, series: pd.Series):
        self.prev_low = analysis.get_prev_low(series=series)
        return self.prev_low

    def get_max_drawdown(self, A=1000):
        if self.wealth_index is None or self.prev_high is None:
            self.get_wealth_index(A=A)
            self.get_prev_high(self.wealth_index)
        self.drawdown = analysis.calculate_max_drawdown(wealth_index=self.wealth_index, prev_high=self.prev_high)
        return self.drawdown

    def get_skewness(self):
        self.skewness = analysis.get_skewness(series=self.returns)
        return self.skewness

    def get_kurtosis(self, excess=False):
        # normal (non-excess) kurtosis is 3
        self.kurtosis = analysis.get_kurtosis(series=self.returns, excess=excess)
        return self.kurtosis
