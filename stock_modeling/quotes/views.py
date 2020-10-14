from django.shortcuts import render
from .data_retriever import *
from .stock_models import *
from .plotting import *

# Create your views here.
def home(request):
	import requests
	import json

	# NJFJY7DW1WXTJ4U4 -- alphavantage
	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_164c554030a54634b6851c5dec4dbe97")

		# Retrieve historical stock data 
		data = retrieve(ticker)

		# make basic plot of historical stock price datap 
		historical_price_plot = saveBasicPlot(data, "quotes/plots", "historical_plot.jpg")

		# models
		(arma, arma_res) = ARMA_model(data)
		(arima, arima_res) = ARIMA_model(data)

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})
		
	else:
		return render(request, 'home.html', {'ticker': "Enter a ticker symbol above."})

def about(request):
	return render(request, 'about.html', {})

def form(request):
	return render(request, 'form.html', {})
