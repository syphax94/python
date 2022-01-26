
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


aipa = web.get_data_yahoo("AI.PA",
                        start = "2009-01-01",
                        end = "2022-1-26")
                        
                        
confidence_interval = float(input('Confidence Interval:'))
days = int(input('Time Horizon: '))

confidence_interval = stats.norm.ppf(confidence_interval/100)
days = np.sqrt(days/250)
vol = data['return'].std()

VaR = vol * confidence_interval * days *100
               

print('\n')
print("The Value at Risk of AIR LIQUIDE is {0:.4f}%".format(VaR))
print("The Value at Risk of AIR LIQUIDE is {0:.2f} USD".format((VaR/100)*1000000/100))
# résultat (screen 1)
```

![alt text](https://i.ibb.co/CMZHdYN/screen-01.png)

Merci pour votre lecture.
Sifax
