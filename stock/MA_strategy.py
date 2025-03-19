import pandas as pd

# 讀取 CSV 檔案
file_path = "./0050_stocks_5y.csv"
df = pd.read_csv(file_path, index_col=0, parse_dates=True, date_format="%Y-%m-%d")
df.dropna(inplace=True)  # 移除无法解析的日期行

# 确保日期格式正确，并按日期排序
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(["Ticker", "Date"])  # 按 Ticker 和 Date 升序排列

below_ma20_stocks = []

# 遍历所有股票（Ticker）
for ticker, group in df.groupby("Ticker"):
    # 确保收盘价是浮点数
    group["Close"] = pd.to_numeric(group["Close"], errors="coerce")

    # 计算 5 日均线
    group[f"{ticker}_MA20"] = group["Close"].rolling(window=20).mean()

    # 取最后一天数据
    last_close = group["Close"].iloc[-1]
    last_ma20 = group[f"{ticker}_MA20"].iloc[-1]

    print(f"{ticker}: Last Close={last_close}, Last MA20={last_ma20}")

    # 判斷是否低於五日均線
    if pd.notna(last_close) and pd.notna(last_ma20) and last_close > last_ma20:
        below_ma20_stocks.append(ticker)

print("未跌破 20 日均线的股票:", below_ma20_stocks)