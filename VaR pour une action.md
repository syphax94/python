
### Value At Risk

La VaR mesure la pire perte attendue sur un horizon donné dans des conditions normales de marché à un niveau de confiance donné.

### Calucul de la VaR
Supposons que notre portefeuille se compose de 5 actions d'une valeur de 10 000 $ 
- AIR LIQUIDE (AI.PA) 
- Compagnie de Saint-Gobain S.A. (SGO.PA)
- Alstom SA (ALO.PA)
- VINCI SA (DG.PA)
- Safran SA (SAF.PA)


```python 
import pandas as pd
import numpy as np
import pandas_datareader as web
from scipy.stats import norm

def Port_VaR(start_date, end_date, stocks, exposure, confidence_interval, Days):
    stock = pd.DataFrame()
    stock = web.DataReader(stocks,
                           start= start_date, 
                           end= end_date,
                           data_source="yahoo")['Close']
    stock_return = stock.pct_change()
    stock_vol = stock_return.std()
    CL = norm.ppf(confidence_interval/100)
    
    # Portfolio Variance Covariance Matrix
    stock_cov = np.array(stock_return.cov())
    
    # Stocks Weightage
    weights = np.array(exposure)/sum(exposure)
    weight_mat = np.mat(weights)
    
    # Portfoltio Variance
    port_var = (weight_mat * stock_cov) * weight_mat.T
    
    # Portfoltio VaR
    port_VaR = np.sqrt(port_var) * CL * np.sqrt(Days)
    
    print("The total exposure for Portfolio is ", "{0:,.2f}".format(sum(exposure)),"USD")
    
    print("{} day Portfolio VaR at {}% Confidence Interval".format(Days,confidence_interval), "is", port_VaR*100)
     
    print("{} day Portfolio VaR at {}% Confidence Interval".format(Days,confidence_interval), "is USD", port_VaR*sum(exposure))


Port_VaR('2021-1-1', '2022-1-26', ['AI.PA', 'SGO.PA', 'ALO.PA', 'DG.PA','SAF.PA'], [2000, 2000, 2000, 2000, 2000], 99, 1)
# résultat(screen 1)
```

![alt text](https://i.ibb.co/BngB8Dr/screen-01.png)

```
VaR au seuil de confiance de 99% à 1 jour, égale à 267,69$, signifie qu'il y a 99% de chances pour que la pertes associée à la détention des actifs composant le Portfeuille n'excéde pas 267,69$.
```
