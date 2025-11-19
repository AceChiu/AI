import numpy as np
import pandas as pd
import yfinance as yf

def get_stock_data(ticker, period="5y"):
    df = yf.download(ticker, period=period, auto_adjust=False)
    if df.empty:
        raise ValueError("⚠️ Yahoo Finance 没有下载到数据，检查股票代码或网络连接")
    return df

//波動率
def calculate_volatility(df, window=252):
    df["Returns"] = df["Close"].pct_change()
    df["Volatility"] = df["Returns"].rolling(window=window, min_periods=1).std() * np.sqrt(window)
    return df

def generate_signals(df, vol_threshold=0.2, short_window=50, long_window=200):
    df["Short_MA"] = df["Close"].rolling(window=short_window, min_periods=1).mean()
    df["Long_MA"] = df["Close"].rolling(window=long_window, min_periods=1).mean()
    df["Signal"] = 0  # 初始化信号

    # **低波动策略**
    low_volatility_idx = df["Volatility"] < vol_threshold
    df.loc[low_volatility_idx, "Signal"] = np.where(
        df.loc[low_volatility_idx, "Short_MA"].to_numpy() > df.loc[low_volatility_idx, "Long_MA"].to_numpy(), 
        1, 
        -1
    )

    # **高波动策略**
    high_volatility_idx = df["Volatility"] >= vol_threshold
    subset_df = df.loc[high_volatility_idx, ["Close", "Short_MA"]]

    return df

# 运行代码
ticker = "AAPL"
df = get_stock_data(ticker)
df = calculate_volatility(df)
df = generate_signals(df)

print(df.tail(10))  # 打印最后 10 行结果
