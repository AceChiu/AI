import yfinance as yf
import pandas as pd
import numpy as np

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

# testReadFile()
# testMaxAndMin()
# testPtp()
# testAVG()
# testMedian()
# testVar()
testVolatility()