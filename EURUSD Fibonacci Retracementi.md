Dans ce cas pratique, un ami effectue l'achat EURUSD.

![alt text](https://www.zupimages.net/up/22/05/znnl.png)

Nous allons analyser qu'elle était la tendance du marché 

Position 1: 1.14762

Position 2: 1.14715

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web

EURUSD = web.DataReader('EURUSD=X','yahoo')

maximum_price = EURUSD['Close'].max()
minimum_price = EURUSD['Close'].min()

difference = maximum_price - minimum_price
first_level = maximum_price - difference * 0.236
second_level = maximum_price - difference  * 0.382
third_level = maximum_price - difference * 0.5
fourth_level = maximum_price - difference * 0.618

new_EURUSD = EURUSD


plt.figure(figsize=(12,6))
plt.title('Fibonacci Retracement EURUSD',fontsize=20)
plt.xlabel('Date', fontsize=17)
plt.ylabel('Price (USD)', fontsize=17)



plt.plot(new_EURUSD.index, new_EURUSD['Close'],color='black')

plt.axhline(maximum_price, linestyle='--' , alpha = 0.5, color='red')
plt.axhline(first_level, linestyle='--' , alpha = 0.5, color='orange')
plt.axhline(second_level, linestyle='--' , alpha = 0.5, color='yellow')
plt.axhline(third_level, linestyle='--' , alpha = 0.5, color='green')
plt.axhline(fourth_level, linestyle='--' , alpha = 0.5, color='blue')
plt.axhline(minimum_price, linestyle='--' , alpha = 0.5, color='purple')

plot.show()

```

![alt text](https://www.zupimages.net/up/22/04/wwrt.png)

!not done yet!
