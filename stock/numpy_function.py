import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as datetime
import matplotlib.dates as mdates


# # 定義股票代碼
# ticker = "2330.TW"

# # 下載過去五年的數據
# df = yf.download(ticker, period="5y")

# # 顯示前五筆數據
# print(df.head())

# # 存成 CSV（如果需要）
# df.to_csv("2330_stock_data.csv")


def testReadFile():
    file_name = "./2330_stock_data.csv"

    end_price, volume = np.loadtxt(
        fname=file_name,
        delimiter=',',
        usecols=(1, 5), 
        unpack=True,
        skiprows=1 
    )

    print("close_price:", end_price)
    print("volume:", volume)  

def testMaxAndMin():
    file_name = "./2330_stock_data.csv"

    high_price, low_price = np.loadtxt(
        fname=file_name,
        delimiter=',',
        usecols=(2, 3), 
        unpack=True,
        skiprows=1 
    )

    print("max_price:", high_price.max())
    print("min_price:", low_price.min())

def testPtp():
    file_name = "./2330_stock_data.csv"

    high_price, low_price = np.loadtxt(
        fname=file_name,
        delimiter=',',
        usecols=(2, 3), 
        unpack=True,
        skiprows=1 
    )

    print("max - min of high price:", np.ptp(high_price))
    print("max - min of low price:", np.ptp(low_price))
    
def testAVG():
    file_name = "./2330_stock_data.csv"

    end_price, volume  = np.loadtxt(
        fname=file_name,
        delimiter=',',
        usecols=(1, 5), 
        unpack=True,
        skiprows=1 
    )

    print("ave_price:", np.average(end_price))
    print("VWAP:", np.average(end_price,weights=volume))

def testMediam():
    file_name = "./2330_stock_data.csv"

    end_price, volume  = np.loadtxt(
        fname=file_name,
        delimiter=',',
        usecols=(1, 5), 
        unpack=True,
        skiprows=1 
    )

    print("median_price:", np.median(end_price))

def testVar():
    file_name = "./2330_stock_data.csv"

    end_price, volume  = np.loadtxt(
        fname=file_name,
        delimiter=',',
        usecols=(1, 5), 
        unpack=True,
        skiprows=1 
    )

    print("var:", np.var(end_price))
    print("var:", end_price.var())

def testVolatility():
    file_name = "./2330_stock_data.csv"

    end_price, volume  = np.loadtxt(
        fname=file_name,
        delimiter=',',
        usecols=(1, 5), 
        unpack=True,
        skiprows=1 
    )
    log_return = np.diff(np.log(end_price))
    annual_volatility = log_return.std() * np.sqrt(250)
    monthly_volatility = log_return.std()  * np.sqrt(12)

    print("log_return:", log_return[:5])
    print("annual_volatility:", annual_volatility)
    print("monthly_volatility:", monthly_volatility)

def testSMA():
    file_name = "./2330_stock_data.csv"

    # 读取数据，确保日期列是字符串，价格列是浮点数
    data = np.loadtxt(
        fname=file_name,
        delimiter=',',
        usecols=(0, 1), 
        dtype=str,  # 先把所有数据读入为字符串
        unpack=True,
        skiprows=1
    )

    raw_date = data[0]  # 日期列
    end_price = data[1].astype(float)  # 转换价格列为浮点数

    date = np.array([datetime.datetime.strptime(d, "%Y-%m-%d") for d in raw_date])

    N_values = [5, 20, 60]  # 定义不同的 SMA 计算周期
    colors = ['r', 'g', 'b']  # 颜色分别用于 5, 20, 60 日 SMA
    labels = ['SMA-5', 'SMA-20', 'SMA-60']  # 线条标签
    
    plt.figure(figsize=(12, 6))
    plt.plot(date, end_price, color='gray', label='Stock Price', alpha=0.5)  # 画出原始价格曲线

    for N, color, label in zip(N_values, colors, labels):
        weights = np.ones(N) / N
        sma = np.convolve(weights, end_price.astype(float), mode='valid')  # 计算 SMA
        sma_dates = date[N-1:]  # 对应的日期要裁剪

        plt.plot(sma_dates, sma, color=color, linewidth=2, label=label)  # 绘制 SMA 线

    # 设置 X 轴格式，使日期美观
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # 格式化 X 轴
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())  # 自动选择适合的刻度
    plt.xticks(rotation=45)  # 旋转 X 轴标签，避免重叠

    plt.legend()
    plt.title("Stock Price and SMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)  # 添加网格
    plt.show()


# testReadFile()
# testMaxAndMin()
# testPtp()
# testAVG()
# testMedian()
# testVar()
# testVolatility()
testSMA()