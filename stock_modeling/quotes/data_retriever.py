import numpy as np
import yfinance as yf

def retrieve(ticker_str, strt_date="2015-06-01", end_date="2020-01-01", ohlc='Close'):

	# columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
	data = yf.download(ticker_str, start=strt_date, end=end_date)

	# get returns from data
	returns_data = np.log(data[ohlc])
	returns_data = returns_data.diff()
	returns_data = returns_data.drop(data.index[0])
	
	return (data, returns_data)