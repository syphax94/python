### Value At Risk

La VaR mesure la pire perte attendue sur un horizon donné dans des conditions normales de marché à un niveau de confiance donné.

```python 

```


### Calucul de la VaR

Différentes méthodes sont utilisées pour le calcul de la VaR. Dans ce cas nous utilision de l'approche variance-covariance et de la méthode de simulation historique pour le calcul de la VaR.



```python 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import pandas_datareader as web

from datetime import datetime
from scipy.stats import norm

aipa = web.get_data_yahoo("AI.PA",
                        start = "2018-01-01",
                        end = "2022-1-25")
                        
 
 rets = (aipa['Close']/aipa['Close'].shift(1))-1
 
mean = np.mean(rets)
std = np.std(rets)
n = norm.ppf(1-0.99) # vérifié si c'est le bon code c pas (0.99)
price = aipa.iloc[-1]['Close']

print(mean, std, n, price) # screen 1

ParamVAR = price*Z_99*std
HistVAR = price*np.percentile(rets_1.dropna(),1)

print('Parametric VAR is {0:.3f} and Historical VAR is {1:.3f}'
         .format(ParamVAR, HistVAR))  # screen 2

np.random.seed(42)
n_sims = 1000000
sim_returns = np.random.normal(mean, std, n_sims)
SimVAR = price*np.percentile(sim_returns, 1)
print('Simulated VAR is', SimVAR) # screen 3

 
```

* screen 1

![alt text](https://i.ibb.co/m8p82cF/screen-01.png)


* screen 2

![alt text](https://i.ibb.co/gMfy5X5/screen-02.png)


* screen 3

![alt text](https://i.ibb.co/CtsdbdD/screen-03.png)


Merci pour votre lecture.
Sifax
