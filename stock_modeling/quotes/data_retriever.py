import yfinance as yf

def retrieve(ticker_str, strt_date, end_date, ohlc='Close'):

	data = yf.download(ticker_str, start=strt_date, end=end_date)

	# columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
	return data