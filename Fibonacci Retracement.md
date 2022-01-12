# Les Retracements de Fibonacci

Le retracement Fibonacci est une méthode employée pour déterminer les niveaux de résistance et support potentiels du prix d’un actif. 
Il se base sur l’idée que le prix retracera une partie prédictible d’un mouvement original, après lequel il continue à se déplacer dans la direction originale.
Historiquement, les plus communes zones de retracement ont été 38.2%, 50% et 61.8%. 
Ces niveaux sont où la majorité des analystes se concentrent, parce qu’ils agissent dans le marché comme un tournant potentiel.
Les retracements Fibonacci peuvent être très efficaces pour faire une chronologie des entrées dans la direction de la tendance.


# Nous allons maintenant analyser la tendance pour l'action AIR LIQUIDE à l'aide du Retrecement de Fibonacci 

```python
import pandas as pd
import pandas_datareader as web
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
```

* Remarque : il est  important d'installer yfinance et datetime afin que le script puisse fonctionner pour cela il nous suffit d'écrire cette commande !pip install yfinance, !pip install datetime

Nous allons indiquer à yahoo finance le ticket=AI.PA qui représente AIR LIQUIDE, ainsi que la date de début et de fin (start,end)

t= Période de 5 ans

```python
df = yf.download('AI.PA', start ="2018-01-01", end="2022-1-07")
```

La commande df va nous afficher un tableau avec des valeurs économiques sur les 5 dérnières années
```python
df
```

* screen 1
![alt text](https://i.ibb.co/smB4fKy/screen1.png)
