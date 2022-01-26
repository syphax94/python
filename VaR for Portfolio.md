
### Value At Risk

La VaR mesure la pire perte attendue sur un horizon donné dans des conditions normales de marché à un niveau de confiance donné.

### Calucul de la VaR pour un portefeuille
Supposons que notre portefeuille se compose de 5 actions d'une valeur de 10 000 $ 
- AIR LIQUIDE (AI.PA) 
- Compagnie de Saint-Gobain S.A. (SGO.PA)
- Alstom SA (ALO.PA)
- VINCI SA (DG.PA)
- Safran SA (SAF.PA)

### Code 
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
    
    print("{} day Portfolio VaR at {}% Confidence Interval".format(Days,confidence_interval), "is", port_VaR)
     
    print("{} day Portfolio VaR at {}% Confidence Interval".format(Days,confidence_interval), "is USD", port_VaR*sum(exposure))


Port_VaR('2009-1-1', '2022-1-26', ['AI.PA', 'SGO.PA', 'ALO.PA', 'DG.PA','SAF.PA'], [2000, 2000, 2000, 2000, 2000], 99, 1)
# résultat(screen 1)

tickers = ["AI.PA", "SGO.PA", "ALO.PA", "DG.PA","SAF.PA"]
multpl_stocks = web.get_data_yahoo(tickers,
start = "2009-1-1",
end = "2022-1-26")

# Tracer les prix des actions du portefeuille
fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax1.plot(multpl_stocks['Close']['AI.PA'])
ax1.set_title("AIR LIQUIDE ")
ax2.plot(multpl_stocks['Close']['SGO.PA'])
ax2.set_title("Compagnie de Saint-Gobain SA")
ax3.plot(multpl_stocks['Close']['ALO.PA'])
ax3.set_title("Alstom SA")
ax4.plot(multpl_stocks['Close']['DG.PA'])
ax4.set_title("VINCI SA")
ax5.plot(multpl_stocks['Close']['SAF.PA'])
ax5.set_title("Safran SA")
plt.tight_layout()
plt.show()   # screen 2

# Calcul des rendements pour plusieurs actions
multpl_stock_daily_returns = multpl_stocks['Close'].pct_change()
multpl_stock_monthly_returns = multpl_stocks['Close'].resample('M').ffill().pct_change()

print(multpl_stock_monthly_returns.mean()) # screen 3

print(multpl_stock_monthly_returns.std()) # screen 4

# Calcul de la corrélation et de la covariance
print(multpl_stock_monthly_returns.corr()) # screen 5

print(multpl_stock_monthly_returns.cov()) # screen 6

```

Screen 1

![alt text](https://i.ibb.co/0rqxxMw/screen-01.png)


La VaR au seuil de confiance de 99% à 1 jour, égale à 353,61$, signifie qu'il y a 99% de chances pour que la pertes associée à la détention des actifs composant le Portfeuille n'excéde pas 353,61$.

Screen 2

![alt text](https://i.ibb.co/rpWsf9N/screen-02.png)

Merci pour votre lecture.

Sifax
