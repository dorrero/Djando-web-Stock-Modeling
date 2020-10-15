import yfinance as yf

<<<<<<< HEAD
def retrieve(ticker_str, strt_date="2015-06-01", end_date="2020-01-01", ohlc='Close'):
=======
def retrieve(ticker_str, strt_date, end_date, ohlc='Close'):
>>>>>>> 0550e9c57e19f139c6c67b1d0b2929643eae5a2f

	data = yf.download(ticker_str, start=strt_date, end=end_date)

	# columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
	return data