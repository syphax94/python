
### Value At Risk

La VaR mesure la pire perte attendue sur un horizon donné dans des conditions normales de marché à un niveau de confiance donné.

### Calucul de la VaR

Différentes méthodes sont utilisées pour le calcul de la VaR. Dans ce cas nous utilision de l'approche variance-covariance et de la méthode de simulation historique pour le calcul de la VaR.

### Code

```python 
import pandas as pd
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
from scipy import stats

data = web.DataReader(['AI.PA'], data_source='yahoo', 
                                start='2009-01-01', 
                                end='2022-1-26')['Close']
                                
data['return'] = np.log(data['AI.PA'] / data['AI.PA'].shift(-1))                                

# Calculate Valute at Risk
# VaR = Volatility * Confidence Interval * sqrt(Time)

# Volatility
vol = data['return'].std() 

# Confidence Interval
confidence_interval = stats.norm.ppf(0.99)

# Calculate Valute at Risk
VaR = confidence_interval * vol *np.sqrt(1) 

#print("The Value at Risk of AIR LIQUIDE is {0:,.2f} USD".format(VaR*1000000/100))


```

![alt text](https://i.ibb.co/HKNJBPq/screen-01.png)

La VaR au seuil de confiance de 99% à 1 jour, égale à 20,10$, signifie qu'il y a 99% de chances pour que la pertes associée à la détention de l'action AIR LIQUIDE n'excéde pas 20,10$.

Merci pour votre lecture.
Sifax
