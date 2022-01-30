# Les Retracements de Fibonacci

Le retracement Fibonacci est une méthode employée pour déterminer les niveaux de résistance et support potentiels du prix d’un actif. 

Il se base sur l’idée que le prix retracera une partie prédictible d’un mouvement original, après lequel il continue à se déplacer dans la direction originale.

Historiquement, les plus communes zones de retracement ont été 38.2%, 50% et 61.8%. Ces niveaux sont où la majorité des analystes se concentrent, parce qu’ils agissent dans le marché comme un tournant potentiel.

Les retracements Fibonacci peuvent être très efficaces pour faire une chronologie des entrées dans la direction de la tendance.


# Analyser la tendance pour l'action AIR LIQUIDE

```python
import pandas as pd
import pandas_datareader as web
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

aipa = yf.download('AI.PA', start ="2018-01-01", end="2022-1-07")

maximum_price = aipa['Close'].max()
minimum_price = aipa['Close'].min()

difference = maximum_price - minimum_price
first_level = maximum_price - difference * 0.236
second_level = maximum_price - difference  * 0.382
third_level = maximum_price - difference * 0.5
fourth_level = maximum_price - difference * 0.618

 print('Level Percentage Price($)')
 print('00.0%\t\t', maximum_price)
 print('23.6%\t\t', first_level)
 print('38.2%\t\t', second_level)
 print('50.0%\t\t', third_level)
 print('61.8%\t\t', fourth_level)
 print('100%\t\t', minimum_price) 


new_aipa = df
plt.figure(figsize=(12,4))
plt.title('Fibonacci Retracement action AIR LIQUIDE',fontsize=20)
plt.xlabel('Date', fontsize=17)
plt.ylabel('Price (USD)', fontsize=17)
plt.plot(new_aipa.index, new_aipa['Close'],color='black')
plt.axhline(maximum_price, linestyle='--' , alpha = 0.5, color='red')
plt.axhline(first_level, linestyle='--' , alpha = 0.5, color='orange')
plt.axhline(second_level, linestyle='--' , alpha = 0.5, color='yellow')
plt.axhline(third_level, linestyle='--' , alpha = 0.5, color='green')
plt.axhline(fourth_level, linestyle='--' , alpha = 0.5, color='blue')
plt.axhline(minimum_price, linestyle='--' , alpha = 0.5, color='purple')

plt.show()
```

# Level Percentage Price
![alt text](https://i.ibb.co/56sC1Qj/11.png)

# Fibonacci Retracement action AIR LIQUIDE
![alt text](https://i.ibb.co/nP0dh4D/12.png)

* Afin d'apporter une meilleure lecture du graphe nous allons apporter quelques modifications au code.


![alt text](https://i.ibb.co/rZdLgmY/1.png)


# Tendance sur 3 mois

![alt text](https://i.ibb.co/tD9DqvF/screen6.png)

# Tendance sur ~ 30 jours

![alt text](https://i.ibb.co/Czd4GLb/screen7.png)



