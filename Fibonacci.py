# Calculate the Fibonacci Retracement Level Prices 

maximum_price = df['Close'].max()
minimum_price = df['Close'].min()

difference = maximum_price - minimum_price
first_level = maximum_price - difference * 0.236
second_level = maximum_price - difference  * 0.382
third_level = maximum_price - difference * 0.5
fourth_level = maximum_price - difference * 0.618

 # Print the price at each level
 print('Level Percentage Price($)')
 print('00.0%\t\t', maximum_price)
 print('23.6%\t\t', first_level)
 print('38.2%\t\t', second_level)
 print('50.0%\t\t', third_level)
 print('61.8%\t\t', fourth_level)
 print('100%\t\t', minimum_price) 
 
 # Plot the Fibonacci Level Prices along with the Close Price

new_df = df
plt.figure(figsize=(12,4))
plt.title('Fibonacci Retracement Plot',fontsize=38)
plt.xlabel('Date', fontsize=28)
plt.ylabel('Price (USD)', fontsize=28)


plt.plot(new_df.index, new_df['Close'],color='black')

plt.axhline(maximum_price, linestyle='--' , alpha = 0.5, color='red')
plt.axhline(first_level, linestyle='--' , alpha = 0.5, color='orange')
plt.axhline(second_level, linestyle='--' , alpha = 0.5, color='yellow')
plt.axhline(third_level, linestyle='--' , alpha = 0.5, color='green')
plt.axhline(fourth_level, linestyle='--' , alpha = 0.5, color='blue')
plt.axhline(minimum_price, linestyle='--' , alpha = 0.5, color='purple')

plt.show()
