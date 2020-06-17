import numpy as np 
import pandas as pd 

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
    Discretize the percentage return into three categories, -1, 0, 1. 
        -1 : if the return us less than -0.5% 
         1 : if it is greater than 0.5% 
         0 : otherwise
    Must be called after calculate_return() function
    

    Parameters
    ----------
    df : pandas.DataFrame
        It needs to have with a column named 'percentage_return'.

    Returns
    -------
    pandas.DataFrame
        same df but percentage_return column is replaced with the categorized label column        

    '''
    
    df.loc[df.percentage_return <= -0.5, 'label'] = '-1'
    df.loc[df.percentage_return >= -0.5, 'label'] = '1'
    df.loc[(df.percentage_return > -0.5) & (df.percentage_return < 0.5), 'label'] = '0' 
    df.drop('percentage_return', axis=1, inplace=True)
    
    return df[19:]