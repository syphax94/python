
### Value At Risk

La VaR mesure la pire perte attendue sur un horizon donné dans des conditions normales de marché à un niveau de confiance donné.

### Calucul de la VaR

```python 
import pandas as pd
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
from scipy import stats

aipa = web.DataReader(['AI.PA'], data_source='yahoo', 
                                start='2009-01-01', 
                                end='2022-1-28')['Close']
                                
aipa['return'] = np.log(data['AI.PA'] / data['AI.PA'].shift(-1))   

# Volatility
vol = aipa['return'].std()

# Confidence Interval
confidence_interval = stats.norm.ppf(0.99)

# VaR = Volatility * Confidence Interval * sqrt(Time)
VaR = confidence_interval * vol *np.sqrt(1/250) 

print('Volatility: {0:.4f}'.format(vol))
print('Confidend Interval: {0:.4f}'.format(confidence_interval))
print("VaR is {0:.2f}".format(VaR*100),'%')
print("The Value at Risk of AIR LIQUIDE is {0:,.2f} USD".format(VaR*1000000/100))


```

![alt texxt](https://i.ibb.co/7vR7yB8/1.png)

La VaR au seuil de confiance de 99% à 1 jour, égale à 20,10$, signifie qu'il y a 99% de chances pour que la pertes associée à la détention de l'action AIR LIQUIDE n'excéde pas 20,10$.

Merci pour votre lecture.

Sifax
