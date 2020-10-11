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



# def arma_model(data):
# 	model = sm.tsa.arima_model.ARMA(, (5, 5))

def ARMA_model(data, ohlc='Close'):

	cleaned_data = np.log(data[ohlc])
	cleaned_data = cleaned_data.diff()
	cleaned_data = cleaned_data.drop(data.index[0])

	params = bestParams(cleaned_data);
	model = sm.tsa.arima_model.ARMA(cleaned_data, (params[0], params[2])).fit()

	results = model.predict(start=50, end=1050)
	return results

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
	    
	result_df = optimize_ARIMA(order_list, exog=data)
	return result_df['(p, d, q)'].iloc[0]

def optimize_ARIMA(order_list, exog):
    """
        Return dataframe with parameters and corresponding AIC
        
        order_list - list with (p, d, q) tuples
        exog - the exogenous variable
    """
    
    results = []
    
    for order in order_list: #tqdm_notebook(order_list):
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