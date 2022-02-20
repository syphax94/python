### Sharpe Ratio

```python
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import numpy as np



def Sharpe_Ratio(cumu_return, rfr, volatility):
    sharpe_ratio = (cumu_return - rfr) / volatility
    return sharpe_ratio


data = pdr.DataReader('AI.PA',data_source='yahoo', start='2021-1-1', end='2022-2-18')
data_close = data['Close']
daily_return = data_close.pct_change()
mean = np.mean(daily_return)
std = np.std(daily_return)
rfr = 0.00693 # 2022-02-17
cumu_return = (data_close[-1]/data_close[0]) -1
volatility = std * np.sqrt(252)


print('-----------------------------------')
print('  Parametres :')
print('---------------')
print('Risk free rate =',rfr)
print('Cumulative Return = {0:.5f}'.format(cumu_return))
print('Volatility = {0:.5f}'.format(volatility))
sharpe_ratio = Sharpe_Ratio(cumu_return, rfr, volatility)
print('-----------------------------------')
print('  Sharpe Ratio :')
print('---------------')
print('Sharpe Ratio is: {0:.2f}'.format(sharpe_ratio),'%')
print('-----------------------------------')
```
![alt text](https://www.zupimages.net/up/22/07/brgs.png)
