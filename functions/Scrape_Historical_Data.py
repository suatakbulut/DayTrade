import pandas as pd 
import numpy as np 
from datetime import date, timedelta
import requests 
import os 

def scrape_historical_data(stock_code):

    '''
    Downloads the 10 year historical price data for stock_code from nasdaq's website. 
    Saves it as a .csv file in 'historical_price_data' folder. 

    Parameters
    ----------
    stock_code : string
        Stock code of a company, preferrably listed in S&P500 index 

    Returns
    -------
    None.

    '''
    directory = 'historical_price_data' 
    if not os.path.exists(directory): 
        os.makedirs(directory)

    today = date.today()
    from_ = today - timedelta(days=10*365+2)

    url_first_part = 'https://www.nasdaq.com/api/v1/historical/'
    url_last = '/stocks/{}/{}'.format(from_, today)
    my_url = url_first_part + stock_code + url_last 

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'}
    page_response = requests.get(my_url, allow_redirects=True, headers=headers)

    file_name = '{}/{}.csv'.format(directory, stock_code)
    with open(file_name, 'wb') as f: 
        for line in page_response:
            f.write(line)
    print('Historical price data for {} is scraped.'.format(stock_code))
