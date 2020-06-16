import numpy as np 
import pandas as pd 
import math 

def cleaner(df):
	'''
	Gets rid of the Volume column,
	rename the remaining columns without having spaces around them,
	sorts the dataframe based on Date, assuming Date is the index

	Parameters
	----------
	df : uncleaned (pandas dataframe),
				that is loaded directly from the .csv file.
	    
	Returns
	-------
	df : (pandas dataframe) cleaned.

	'''	
	df.drop([' Volume'], axis=1, inplace=True)
	df.columns = ['Date', 'Close', 'Open', 'High', 'Low']
	df.set_index(pd.to_datetime(df.Date),  inplace=True)
	df.drop('Date', axis=1, inplace=True)
	df.sort_index(inplace = True)
	df[df.columns] = df[df.columns].replace('[\$,]', '', regex=True).astype(float)

	return df 

#------------------------------------------------------

def calculate_return(df): 
    '''
    Calculates the percentage return when bought today at Close 
    price and sold tomorrow at Close price.
    
    Parameters
    ----------
    stockprices : pandas dataframe
    
    Returns
    -------
    	percentage_return (np.array): has a length of len(df)-1
    
    '''	
    	
    today = np.array(df[:-1].Close) 
    tomorrow = np.array(df[1:].Close) 
    percentage_return = 100*(tomorrow - today)/today 
    df.loc[:-1,'percentage_return'] = percentage_return
    return df[:-1]

#------------------------------------------------------

def categorizer(df):
	'''
	Creates bins of length 0.5 from -3 to +3.5. 
	Any percentage return that falls into a bin is called 
	by the same number, that is ceil(2*return)
	any return greater than 3.5% is assigned to 7.
	any return smaller than -3% is assgined to -6. 

		<------|----|----|..|..|----|----|---->
		      -3  -2.5   .. 0 ..    3   3.5
	So, there are 14 percentage return bins. 
		-6, -5, -4, ... , 0, ... 5, 6, 7
	
	Parameters
	----------
	df : (pandas dataframe) with a column named 'percentage_return'
	    
	Returns
	-------
	df : (pandas dataframe) that has a columns 'label'
	     with integer vals from -6 to 7 representing 
	     the percentage returns

	'''	
	df.loc[df.percentage_return >= 3.5, 'percentage_return'] = 3.5 
	df.loc[df.percentage_return <= -3, 'percentage_return'] = -3
	
	df['label'] = df.apply(lambda row: math.ceil(2*row.percentage_return), axis=1)
	df.drop('percentage_return', axis=1, inplace=True)
	
	return df[19:]