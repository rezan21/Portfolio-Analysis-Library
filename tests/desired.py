import pandas as pd


class Desired:
    FFME_ANN_RET = {"smallCap": 0.1674632857505609, "largeCap": 0.0928096810826724}
    FFME_PER_PERIOD_RET = {"smallCap": 0.012986371862751644, "largeCap": 0.007423423733719403}
    FFME_ANN_VOL = {"smallCap": 0.3681930492499155, "largeCap": 0.18671598774331255}
    FFME_ANN_SHARPE = {"smallCap": 0.45482467985671604, "largeCap": 0.4970633859713306}
    FFME_ANN_SHARPE_3PCT = {"smallCap": 0.37334568382157596, "largeCap": 0.33639155297734813}
    FFME_WEALTH_INDEX = [1032.8999999, 1071.1173, 1078.2937859, 1052.0912469, 1080.49771057]
    FFME_MAX_DRAWDOWN = {"smallCap": -0.8330007793945303, "largeCap": -0.8400375277943123}
    FFME_MAX_DRAWDOWN_PERIOD = {"smallCap": pd.Period("1932-05", "M"), "largeCap": pd.Period("1932-05", "M")}

    HFI_SEMI_DEV = {
        "Convertible Arbitrage": 0.019539843513132593,
        "CTA Global": 0.012442800321093829,
        "Distressed Securities": 0.015185283870320707,
        "Emerging Markets": 0.02803858208960027,
        "Equity Market Neutral": 0.009566031256119517,
        "Event Driven": 0.015429138379306581,
        "Fixed Income Arbitrage": 0.017762796287444448,
        "Global Macro": 0.006579420166584438,
        "Long/Short Equity": 0.014050967499393425,
        "Merger Arbitrage": 0.008874887364411683,
        "Relative Value": 0.01224417486970012,
        "Short Selling": 0.027283243102571814,
        "Funds Of Funds": 0.012122154739394207,
    }
    HFI_SKEWNESS = {
        "Fixed Income Arbitrage": -3.9403202911900856,
        "Convertible Arbitrage": -2.6395922251089274,
        "Equity Market Neutral": -2.12443538394212,
        "Relative Value": -1.8154697489380176,
        "Event Driven": -1.409153563554795,
        "Merger Arbitrage": -1.3200833333543787,
        "Distressed Securities": -1.30084204379122,
        "Emerging Markets": -1.1670674947992334,
        "Long/Short Equity": -0.39022677418839474,
        "Funds Of Funds": -0.3617830836837326,
        "CTA Global": 0.17369864499039014,
        "Short Selling": 0.7679748443026674,
        "Global Macro": 0.9829218839470765,
    }
    HFI_KURTOSIS = {
        "Convertible Arbitrage": 23.28083445586127,
        "CTA Global": 2.9529603687465187,
        "Distressed Securities": 7.889983357716656,
        "Emerging Markets": 9.250788406118145,
        "Equity Market Neutral": 17.21855525912839,
        "Event Driven": 8.035828166316836,
        "Fixed Income Arbitrage": 29.842199278359708,
        "Global Macro": 5.741679447000011,
        "Long/Short Equity": 4.523892582215413,
        "Merger Arbitrage": 8.73894979181258,
        "Relative Value": 12.121207865164642,
        "Short Selling": 6.11777175096972,
        "Funds Of Funds": 7.07015277555583,
    }
