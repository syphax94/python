# Les Retracements de Fibonacci

Le retracement Fibonacci est une méthode employée pour déterminer les niveaux de résistance et support potentiels du prix d’un actif. 

Il se base sur l’idée que le prix retracera une partie prédictible d’un mouvement original, après lequel il continue à se déplacer dans la direction originale.

Historiquement, les plus communes zones de retracement ont été 38.2%, 50% et 61.8%. 

Ces niveaux sont où la majorité des analystes se concentrent, parce qu’ils agissent dans le marché comme un tournant potentiel.

Les retracements Fibonacci peuvent être très efficaces pour faire une chronologie des entrées dans la direction de la tendance.

* Remarque : il est  important d'installer yfinance et datetime afin que le script puisse fonctionner pour cela il nous suffit d'écrire cette commande !pip install yfinance, !pip install datetime

Nous allons indiquer à yahoo finance le ticker=AI.PA qui représente AIR LIQUIDE, ainsi que la date de début et de fin (start,end)

t= Période de 5 ans

# Nous allons maintenant analyser la tendance pour l'action AIR LIQUIDE à l'aide du Retrecement de Fibonacci 

```python
import pandas as pd
import pandas_datareader as web
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

df = yf.download('AI.PA', start ="2018-01-01", end="2022-1-07")

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


new_df = df
plt.figure(figsize=(12,4))
plt.title('Fibonacci Retracement action AIR LIQUIDE',fontsize=20)
plt.xlabel('Date', fontsize=17)
plt.ylabel('Price (USD)', fontsize=17)
plt.plot(new_df.index, new_df['Close'],color='black')
plt.axhline(maximum_price, linestyle='--' , alpha = 0.5, color='red')
plt.axhline(first_level, linestyle='--' , alpha = 0.5, color='orange')
plt.axhline(second_level, linestyle='--' , alpha = 0.5, color='yellow')
plt.axhline(third_level, linestyle='--' , alpha = 0.5, color='green')
plt.axhline(fourth_level, linestyle='--' , alpha = 0.5, color='blue')
plt.axhline(minimum_price, linestyle='--' , alpha = 0.5, color='purple')

plt.show()
```
* screen 4

![alt text](https://i.ibb.co/GtmTBG3/screen4.png)

* Afin d'apporter une meilleure lecture du graphe nous allons apporter quelques modifications au code

```python
new_df =df
fig = plt.figure(figsize=(20,10))

plt.xlabel('Date', fontsize=17)
plt.ylabel('Price (USD)', fontsize=17)
ax = fig.add_subplot(1, 1, 1)
plt.title('Fibonacci Retracement action AIR LIQUIDE',fontsize=20)  
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
```

* screen 5

![alt text](https://i.ibb.co/yXPGzHr/screen5.png)

# Tendance sur 3 mois
```python
df = yf.download('AI.PA', start ="2021-10-01", end="2022-12-31")
```
* screen 6

![alt text](https://i.ibb.co/tD9DqvF/screen6.png)

# Tendance sur ~ 30 jours
```python
df = yf.download('AI.PA', start ="2021-12-01", end="2022-01-12")
```
* screen 7

![alt text](https://i.ibb.co/Czd4GLb/screen7.png)


Merci pour votre lecture.

Sifax

![alt text](https://i.ibb.co/BLV5zQ0/screen3.png)
