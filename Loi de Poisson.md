### Loi de Poisson
Une variable aléatoire X suit une loi de Poisson de paramétre λ noté X ~>P(λ)

Cas pratique:
Le nombre X d'accidents de travail surviennent annuellement dans une entreprise obéit à une loi de poisson de paramêtre 3.

Calculer la probabilité des évènements suivants:

- aucun accident ne survient pendant l'année
- au moins 4 accidents survienent dans l'année


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web

def fact(x):
    if x == 0:
        return 1
    else:
        return x  * factorielle(n-1)
        
# aucun accident
# P [ X = 0 ] = ((e^-3) * (3^0)) / 0!
p = ((np.exp(-3)) * (3**0)) / fact(0)

print(p)

P= p*100
print('P =', "{:.2f}".format(P),'%')
print('Il y a',"{:.2f}".format(P) ,'% de chance d obtenir aucun accident de travaille')

# au moins 4 accidents surviennent dans l'année
# P [ x >= 4] = 1 - P [x < 4]
#             = 1 - [P[X=0] + P[X=1] + P[X=2] + P[X=3]]
p2 = 1 - (((np.exp(-3)) * (3**0)) / factorielle(0) + ((np.exp(-3)) * (3**1)) / factorielle(1) + ((np.exp(-3)) * (3**2)) / factorielle(2) + ((np.exp(-3)) * (3**3)) / factorielle(3))

print(p2)
P2= p2*100
print('P2 =', "{:.2f}".format(P2),'%')
print('Il y a',"{:.2f}".format(P2), '% de chance d obtenir 4 accidents de travaille')
```
![alt text](https://www.zupimages.net/up/22/04/0s4j.png)

![alt text](https://www.zupimages.net/up/22/04/l5sh.png)
