import yfinance as yf
import pandas as pd

def get_stock_data(ticker, period="3mo"):
    print(f"Feching data for {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df

def analyze_real_stock(ticker):
    df = get_stock_data(ticker)

    latest_close = df["Close"].iloc[-1]
    latest_volume = df["Volume"].iloc[-1]

    df["MA_50"] = df["Close"].rolling(window=50).mean()
    latest_ma_50 = df["MA_50"].iloc[-1]

    first_price = df["Close"].iloc[0]
    period_return = ((latest_close - first_price) / first_price) *100


    print(f"\n{'='*45}")
    print(f"  {ticker} - Real Market Data")
    print(f"{'='*45}")
    print(f"  Latest Price : ${latest_close:.2f}")
    print(f"  MA 50 : ${latest_ma_50:.2f}")
    print(f"  Volume : {latest_volume:,}")
    print(f"  3mo : {period_return:+.2f}%")

    if latest_close > latest_ma_50 :
        print(f"  Trend        : ABOVE MA50 — bullish")
    else:
        print(f"  Trend        : BELOW MA50 — bearish")

    print(f"{'='*45}\n")


watchlist = ["NVDA", "AAPL", "MSFT"]

for ticker in watchlist:
    analyze_real_stock(ticker)