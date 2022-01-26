### Value At Risk

La VaR mesure la pire perte attendue sur un horizon donné dans des conditions normales de marché à un niveau de confiance donné.

### Calucul de la VaR

Différentes méthodes sont utilisées pour le calcul de la VaR. Dans ce cas nous utilision de l'approche variance-covariance et de la méthode de simulation historique pour le calcul de la VaR.

### Code

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
C_1 = norm.ppf(1-0.99) 
C_5 = norm.ppf(1-0.95) 
price = aipa.iloc[-1]['Close']

print('1% Confidence :', mean, std, C_1, price)
print('5% Confidence',mean, std, C_5, price)       # screen 1

ParamVAR_1 = price*C_1
ParamVAR_5 = price*C_5
HistVAR = price*np.percentile(rets.dropna(),1)

print('Parametric VaR for 1% confidence {0:.3f} and Historical VaR is {1:.3}'
         .format(ParamVAR_1, HistVAR))     


print('Parametric VaR for 5% confidence {0:.3f} and Historical VaR is {1:.3}'
         .format(ParamVAR_5, HistVAR)  # screen 2

np.random.seed(42)
n_sims = 1000000
sim_returns = np.random.normal(mean, std, n_sims)
SimVAR = price*np.percentile(sim_returns, 1)
print('Simulated VaR is', SimVAR)
print("The Value at Risk of AIR LIQUIDE is {0:,.2f} USD".format(SimVAR*1000000/100)) # screen 3

 
```

* screen 1

![alt text](https://i.ibb.co/58X4ypN/screen-01.png)


* screen 2

![alt text](https://i.ibb.co/8YLmC9P/screen-02.png)


* screen 3

![alt text](https://i.ibb.co/H2c4HFm/screen-03.png)


Merci pour votre lecture.

Sifax
