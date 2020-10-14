import pandas as pd
import matplotlib.pyplot as plt

def saveBasicPlot(data, path, name):

	fig = plt.figure()
	plt.plot(data.index, data.Close)
	plt.xlabel("Date")
	plt.ylabel("Stock Price")
	plt.title("Trend over Given Range")

	fig.savefig(path + '/' + name)
	return fig