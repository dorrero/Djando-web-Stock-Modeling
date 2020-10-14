import yfinance as yf

def retrieve(ticker_str, strt_date="2019-01-01", end_date="2020-01-01", ohlc='Close'):

	data = yf.download(ticker_str, start=strt_date, end=end_date)

	# columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
	return data