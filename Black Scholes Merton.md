### Black Scholes Merton


```python
import numpy as np
from scipy.stats import norm

def BSM(S, K, sigma, r, T, q):
    d1 = ( np.log(S/K) + ((r - q + sigma**2/2)* T))/ (sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))
    return d1, d2

def Call_price(S, K, sigma, r, T, q):
    call = S*np.exp(-q*T) * norm.cdf(d1) - K*np.exp(-r*T) * norm.cdf(d2)
    return call

def Put_price(S, K, sigma, r, T, q):
    put = K*np.exp(-r*T) * norm.cdf(-d2) - S*np.exp(-q*T) * norm.cdf(-d1)
    return put
S=42
K=40
sigma=0.2
r=0.1
T=0.5
q=0.03
nd_1=norm.cdf(d1)
nd_2=norm.cdf(d2)
nd_n1=norm.cdf(-d1)
nd_n2=norm.cdf(-d2)
nd1=-d1
nd2=-d2
d1, d2 = BSM(S, K, sigma, r, T, q)
call = Call_price(S, K, sigma, r, T, q)
put = Put_price(S, K, sigma, r, T, q)

print('-----------------------------------')
print('  Parametres :')
print('---------------')
print('S =', S)
print('K =', K)
print('sigma =', sigma)
print('r =', r)
print('T =', T)
print('q =', q)
print('-----------------------------------')
print(' Call option :')
print('---------------')
print('d1 ={0:.3f}'.format(d1))
print('N(d1) ={0:.3f}'.format(nd_1))
print('d2 ={0:.3f}'.format(d2))
print('N(d2) ={0:.3f}'.format(nd_2))
print('Call Price is: ${0:.3f}'.format(call))
print('-----------------------------------')
print(' Put option :')
print('---------------')
print('-d1 ={0:.3f}'.format(nd1))
print('N(-d1) ={0:.3f}'.format(nd_n1))
print('-d2 ={0:.3f}'.format(nd2))
print('N(-d2) ={0:.3f}'.format(nd_n2))
print('Put Price is:{0:.3f} $'.format(put))
print('-----------------------------------')
```

![alt text](https://www.zupimages.net)


