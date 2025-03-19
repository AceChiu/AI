import yfinance as yf
import pandas as pd

# 0050 成分股（台湾股票代码需要加 ".TW"）
tickers = [
    "2330.TW", "2317.TW", "2454.TW", "6505.TW", "2412.TW",
    "1301.TW", "3008.TW", "2882.TW", "2881.TW", "2308.TW",
    "1216.TW", "2891.TW", "5871.TW", "2002.TW", "2886.TW",
    "1101.TW", "2884.TW", "2885.TW", "1326.TW", "2379.TW",
    "2357.TW", "2912.TW", "2880.TW", "2207.TW", "2890.TW",
    "3005.TW", "9910.TW", "1590.TW", "2892.TW", "3045.TW",
    "2603.TW", "2327.TW", "3702.TW", "5876.TW", "2408.TW",
    "2201.TW", "2301.TW", "2883.TW", "2356.TW", "4904.TW",
    "6415.TW", "3034.TW", "1102.TW", "3706.TW", "4958.TW",
    "6446.TW", "2382.TW", "9933.TW", "8464.TW", "1513.TW"
]

# 下载所有股票的过去 5 年数据
df = yf.download(tickers, period="5y")
df = df.stack(level=1).reset_index()
df.rename(columns={"level_1": "Ticker"}, inplace=True)

# 查看数据
print(df.head())

# 存储为 CSV
df.to_csv("0050_stocks_5y.csv")
