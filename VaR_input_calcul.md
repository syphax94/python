
### Value at Risk pour l'action AIR LIQUIDE

Ce code permet d'entrer 2 types de données: Confidence Interval & Time Horizon(days).

Puis le calcul de la VaR se fait automatiquement.



### Calucul de la VaR

```python 
import numpy as np
import pandas_datareader as web
from scipy import stats

data = web.get_data_yahoo("AI.PA",
                        start = "2009-01-01",
                        end = "2022-1-26")
                        
 aipa['return'] = np.log(data['AI.PA'] / data['AI.PA'].shift(-1))
 
confidence_interval = float(input('Confidence Interval:'))
days = int(input('Time Horizon: '))

confidence_interval = stats.norm.ppf(confidence_interval/100)
days = np.sqrt(days/250)
vol = aipa['return'].std()

VaR = vol * confidence_interval * days *100
               

print('\n')
print("The Value at Risk of AIR LIQUIDE is {0:.4f}%".format(VaR))
print("The Value at Risk of AIR LIQUIDE is {0:.2f} USD".format((VaR/100)*1000000/100))
# résultat (screen 1)
```

![alt text](https://i.ibb.co/8DVDTY8/1.png)

La VaR au seuil de confiance de 99% à 1 jour, égale à 20,09$, signifie qu'il y a 99% de chances pour que la pertes associée à la détention de l'action AIR LIQUIDE n'excéde pas 20,09$.


