# Calculate the Fibonacci Retracement Level Prices 

import pandas as pd
import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf



tsla = yf.Ticker("TSLA")
his = tsla.history(period="max")


maximum_price = df['Close'].max()
minimum_price = df['Close'].min()

difference = maximum_price - minimum_price
first_level = maximum_price - difference * 0.236
second_level = maximum_price - difference  * 0.382
third_level = maximum_price - difference * 0.5
fourth_level = maximum_price - difference * 0.618


 
 # Plot the Fibonacci Level Prices along with the Close Price

new_df =df
fig = plt.figure(figsize=(20,10))

plt.xlabel('Date', fontsize=28)
plt.ylabel('Price (USD)', fontsize=28)
ax = fig.add_subplot(1, 1, 1)
plt.title('Fibonacci Retracement Plot',fontsize=38)  
plt.plot(new_df.index, new_df['Close'], color='black')

plt.axhline(maximum_price, linestyle='--' , alpha = 0.5, color='red')
ax.fill_between(new_df.index, maximum_price, first_level,alpha = 0.5, color='red')
plt.axhline(first_level, linestyle='--' , alpha = 0.5, color='orange')
ax.fill_between(new_df.index, first_level, second_level, alpha = 0.5, color='orange')
plt.axhline(second_level, linestyle='--' , alpha = 0.5, color='yellow')
ax.fill_between(new_df.index, second_level, third_level, alpha = 0.5, color='yellow')

plt.axhline(third_level, linestyle='--' , alpha = 0.5, color='green')
ax.fill_between(new_df.index, third_level, fourth_level, alpha = 0.5, color='green')

plt.axhline(fourth_level, linestyle='--' , alpha = 0.5, color='blue')
ax.fill_between(new_df.index, fourth_level, minimum_price, alpha = 0.5, color='blue')

plt.axhline(minimum_price, linestyle='--' , alpha = 0.5, color='purple')







plt.show()
