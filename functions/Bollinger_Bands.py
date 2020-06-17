import pandas as pd 

def bollinger_bands(df):
    '''
    Calculates the dailiy bollinger bands' upper and lower limits 
    along with a 20-day moving average for each day.

    Parameters
    ----------
    stockprices (pandas dataframe): that must have a column called
    'Close'. And rows must be sorted datetime. 
        
    Returns
    -------
    df : stockprices with three more columns for lower bollinger,
    upper bollinger, and 20-day moving average. 

    '''

    df['bollingerMA20'] = df['Close'].rolling(window=20).mean()
    df['20dSTD'] = df['Close'].rolling(window=20).std() 

    df['bollingerUpper'] = df['bollingerMA20'] + (df['20dSTD'] * 2)
    df['bollingerLower'] = df['bollingerMA20'] - (df['20dSTD'] * 2)

    return df