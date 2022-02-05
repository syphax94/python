### Hedging Strategies using Futures

Assume that we have to manages a portfolio of $200 million wirth of tech stocks which has a beta of 1.5 relative to the Nasdaq-100.
The current value of the 3 month Nasdaq-100 Index is 2,500, and the multiplier is 300.
Over the next 3 months, we wants to use the Nasdaq-100 futures to reduce the systematic risk of the porfolio to 1.0
To pull that off, wich how many contracts are required?


```python
import numpy as np
import pandas as pd

def Number_of_Contrats_Required(Beta_Portfolio, Beta_Target, P, A):
    NCR = (Beta_Target - Beta_Portfolio) * (P/A)
    return NCR
    
Beta_Portfolio = 1.5
Beta_Target = 1
P = 200000000
A = (2500*300)

NCR = Number_of_Contrats_Required(Beta_Portfolio, Beta_Target, P, A)
print('Number of Contracts Required is:{0:.0f}'.format(NCR))
```
![alt text](https://www.zupimages.net/up/22/05/1gd4.png)

The negative sign implies 133 contracts need to be sold.
