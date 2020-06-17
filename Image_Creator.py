import plotly.graph_objects as go

def image_creator(df, file_name, image_size=256):

  '''
  Generates a .png file named file_name.png of last 22 candles
  along with bollinger bands and 20-day moving average and store 
  it to "images/label/file_name.png". 
  If there is no images/label directory, you must first create it 
  before calling this function

  Parameters
  ----------
  df (pandas dataframe): must have the following columns
                          - Date as index
                          - bollingerUpper
                          - bollingerLower 
                          - Open, Close, High, Low
                          - label 
  
  file_name (string) : ex. 'AAPL_29' 'AAPL_' + start
      
  Returns
  -------
  None 

  '''        
  fig = go.Figure(data=[go.Candlestick(x = df.index , 
                                    open = df.Open , 
                                    high = df.High  , 
                                    low = df.Low , 
                                    close = df.Close  
                                    )])

  fig.add_trace(go.Scatter(x=df.index, y=df.bollingerUpper, 
  					     line = dict(color='red', width=1.5)))
  fig.add_trace(go.Scatter(x=df.index, y=df.bollingerLower, 
  						 line = dict(color='blue', width=1.5)))
  fig.add_trace(go.Scatter(x=df.index, y=df.bollingerMA20, 
  						 line = dict(color='black', width=1.5)))

  fig.update_layout(xaxis_rangeslider_visible=False, 
                    autosize=False, 
                    width=image_size, 
                    height=image_size,
                    xaxis_showgrid=False, 
                    yaxis_showgrid=False,
                    yaxis=dict(ticktext=[], tickvals=[]), 
                    xaxis=dict(ticktext=[], tickvals=[]),
                    showlegend = False
                    )
  label = int(df.iloc[-1].label)
  fig.write_image("images/{}/{}.png".format(label, file_name))
  