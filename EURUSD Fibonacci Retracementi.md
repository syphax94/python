Dans ce cas pratique, un ami effectue l'achat EURUSD.

![alt text](https://www.zupimages.net/up/22/05/znnl.png)

Nous allons analyser qu'elle était la tendance du marché pour une seule position

Position 1: 1.14762



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

position_1 = 1.14762
plt.figure(figsize=(12,6))
plt.title('Fibonacci Retracement EURUSD',fontsize=20)
plt.xlabel('Date', fontsize=17)
plt.ylabel('Price (USD)', fontsize=17)
plt.plot(EURUSD.index, EURUSD['Close'],color='black')
plt.axhline(maximum_price, linestyle='--' , alpha = 0.5, color='red')
plt.axhline(first_level, linestyle='--' , alpha = 0.5, color='orange')
plt.axhline(second_level, linestyle='--' , alpha = 0.5, color='yellow')
plt.axhline(third_level, linestyle='--' , alpha = 0.5, color='green')
plt.axhline(fourth_level, linestyle='--' , alpha = 0.5, color='blue')
plt.axhline(minimum_price, linestyle='--' , alpha = 0.5, color='purple')
plt.axhline(y=position_1,  linestyle='-' , alpha = 0.5, color='red')

plt.show()

```

![alt text](https://www.zupimages.net/up/22/05/l52r.png)
!not done yet!
