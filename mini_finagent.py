portfolio = [
    {"ticker": "NVDA",  "price": 924.50, "buy_price": 800.00, "rsi": 72.5, "ma_50": 880.0},
    {"ticker": "AAPL",  "price": 189.30, "buy_price": 170.00, "rsi": 45.2, "ma_50": 182.0},
    {"ticker": "MSFT",  "price": 378.90, "buy_price": 400.00, "rsi": 28.1, "ma_50": 390.0},
    {"ticker": "GOOGL", "price": 175.20, "buy_price": 160.00, "rsi": 55.8, "ma_50": 168.0},
]

def calculate_return(buy_price, current_price):
    return ((current_price - buy_price) / buy_price) *100
def get_signal(rsi, price, ma_50):
    if rsi > 70 and price > ma_50 :
        return "SELL"
    elif rsi < 30 and price < ma_50 :
        return "BUY"
    else :
        return "HOLD"
def analyze_portfolio(portfolio):
    print("=" * 50)
    print("  FinAgent — Portfolio Analysis")
    print("=" * 50)

    buy_signals = []
    sell_signals = []
    hold_signals = []

    for stock in portfolio:
        signal = get_signal(stock["rsi"], stock["price"], stock["ma_50"])
        gain = calculate_return(stock["buy_price"], stock["price"])

        print(f"\n{stock["ticker"]}")
        print(f"PRICE : {stock['price']}")
        print(f"RSI : {stock['rsi']}")
        print(f"Return : {gain:+.2f}%")
        print(f"Singnal : {signal}")

        if signal == "BUY":
            buy_signals.append(stock["ticker"])
        elif signal == "SELL":
            sell_signals.append(stock["ticker"])
        else:
            hold_signals.append(stock["ticker"])

    print("\n" + "=" * 50)
    print(f"BUY -> {buy_signals}")
    print(f"SELL -> {sell_signals}")
    print(f"HOLD -> {hold_signals}")
    print("=" * 50)

analyze_portfolio(portfolio)