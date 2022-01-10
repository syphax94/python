# Python-

Code Fibonacci en python
#####Un code entier
# Calculate the Fibonacci Retracement Level Prices 

maximum_price = df['Close'].max()
minimum_price = df['Close'].min()

difference = maximum_price - minimum_price
first_level = maximum_price - difference * 0.236
second_level = maximum_price - difference  * 0.382
third_level = maximum_price - difference * 0.5
fourth_level = maximum_price - difference * 0.618
