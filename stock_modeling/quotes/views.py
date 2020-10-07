from django.shortcuts import render

# Create your views here.
def home(request):
	import requests
	import json

	# NJFJY7DW1WXTJ4U4 -- alphavantage
	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_164c554030a54634b6851c5dec4dbe97")
		#api_request = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOGL&apikey=NJFJY7DW1WXTJ4U4")

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