import yfinance as yf

def retrieve(ticker_str):
	yfTicker = yf.Ticker(ticker_str)

	data = yfTicker.history(period="max")
	data = data.drop(columns=["Dividends", "Stock Splits"])

	print(data)
	return data