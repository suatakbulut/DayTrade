# DayTrade_by_DeepLearning

The aim of this project: Predicting the possible outcome of a day trade by training a deep learning model on the image data of historic candle stick charts with some financial indicators drawn on them 

- Data Scraping: 
	For 250 stocks listed in S&P500 index, scraped the historical price data for the last five years. 

- Creating .png images:
	For ever 22 day long interval, draw the candlestick chart of the data along with some financial indicators (bollinger bands for now) on it
	For each image file, created day_trade_precentage feature - calculated as the percentage return of buying the stock at the Close price of the 22nd day (the last day included in the candle stick chart) and selling it at the next day's Close price
	Discretized the percentage return into N many categories. 
		How the categories are created? 
	Save the image files in the directory images/<label> where label is its category

- Preparing Data Directory for flow_from_directory: 
	In order to be able to use flow_from_directory method of Keras, split the data into 3 directories under images_separated directory, called train_data, validation_data, test_data. The structure of the directory is as follows:

	images_separated/
		train_data/
			label_1/
				train1_image_1.png
				train1_image_2.png
				...
			label_2/
				train2_image_1.png
				train2_image_2.png
				...
			...
		validation_data/
			label_1/
				validation1_image_1.png
				validation1_image_2.png
				...
			label_2/
				validation2_image_1.png
				validation2_image_2.png
				...
			...
		test_data/
			label_1/
				test1_image_1.png
				test1_image_2.png
				...
			label_2/
				test2_image_1.png
				test2_image_2.png
				...
			...

- Train CNN model: 
	The architecture of the CNN model is as follows:

- Results: 
	Currently, I have a working simple CNN model that yields an accuracy of 0.18. 
