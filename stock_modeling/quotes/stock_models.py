from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.stattools import acf
from tqdm import tqdm_notebook
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels as sm
from itertools import product
import warnings
warnings.filterwarnings('ignore')

def ARMA_model(data, ohlc='Close'):

	# get returns from data
	returns_data = np.log(data[ohlc])
	returns_data = returns_data.diff()
	returns_data = returns_data.drop(data.index[0])

	# choose best p, q parameters for our model using AIC optimization
	params = bestParams(returns_data)
	model = sm.tsa.arima_model.ARMA(returns_data, (params[0], params[2])).fit()

	model_summary = model.summary().as_text()

	# write summary to file
	fileobj = open("quotes/static/model_results/ARMA_Summary.txt", 'w')
	fileobj.write(model_summary)
	fileobj.close()

	return model

def ARIMA_model(data, ohlc='Close'):

	# get returns from data
	returns_data = np.log(data[ohlc])
	returns_data = returns_data.diff()
	returns_data = returns_data.drop(data.index[0])

	# choose best p, q parameters for our model using AIC optimization
	params = bestParams(returns_data)
	model = sm.tsa.arima_model.ARIMA(returns_data, params).fit()

	model_summary = model.summary().as_text()

	# write summary to file
	fileobj = open("quotes/static/model_results/ARIMA_Summary.txt", 'w')
	fileobj.write(model_summary)
	fileobj.close()

	return model

def bestParams(data):

	ps = range(0, 8, 1)
	d = 1
	qs = range(0, 8, 1)

	# Create a list with all possible combination of parameters
	parameters = product(ps, qs)
	parameters_list = list(parameters)
	order_list = []

	for each in parameters_list:
	    each = list(each)
	    each.insert(1, 1)
	    each = tuple(each)
	    order_list.append(each)

	result_df = AIC_optimization(order_list, exog=data)
	return result_df['(p, d, q)'].iloc[0]

def AIC_optimization(order_list, exog):
    """
        Return dataframe with parameters and corresponding AIC

        order_list - list with (p, d, q) tuples
        exog - the exogenous variable
    """

    results = []

    for order in order_list:
        try:
            model = SARIMAX(exog, order=order).fit(disp=-1)
        except:
            continue

        aic = model.aic
        results.append([order, model.aic])

    result_df = pd.DataFrame(results)
    result_df.columns = ['(p, d, q)', 'AIC']

    #Sort in ascending order, lower AIC is better
    result_df = result_df.sort_values(by='AIC', ascending=True).reset_index(drop=True)
    return result_df