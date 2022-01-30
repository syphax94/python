# La simulation Monte Carlo

 Les simulations de Monte-Carlo sont des algorithmes utilisés dans le but d’estimer la probabilité d’occurrence d’un scénario dans lequel interviennent des paramètres aléatoires. 
 
 C’est une technique statistique permettant de comprendre l’influence de l’incertitude dans les modèles de prédiction, notamment en finance.


# Nous allons prendre l'action AIR LIQUIDE, prix  initial 158.20€

* Volatilité 1.11%
 
![alt text](https://i.ibb.co/FYXdLJV/screen2.png)

* Risk free rate = 0.2340

![alt text](https://i.ibb.co/4fd2J5d/taux-sans-risque.png)

* Beta = 0.57

![alt text](https://i.ibb.co/Hgm0wdc/beta.png)

* Market Return Premium = 1.76%

![alt text](https://i.ibb.co/sg63S3s/market-return-premium.png)

Drift = Excepted Return = Risk free rate + (Beta * Market Return Premium)
                        -> Excepted Return = 0.243% + ( 0.57 * 1.76%)
                        -> Drift = 0.244%

# Code Simulation Monte Carlo

```python
import math
import numpy as np
import matplotlib.pyplot as plt


class European_Call_Payoff:

    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price > self.strike:
            return stock_price - self.strike
        else:
            return 


class GeometricBrownianMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.normal(0, math.sqrt(self.dt))  
            dYt = self.drift*self.dt + self.volatility*dWt 
            self.current_price += dYt  
            self.prices.append(self.current_price)  
            self.T -= self.dt 
    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price      
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()

# Parameters
paths = 100
initial_price = 158.20
drift = .0244
volatility = .0111
dt = 1/250
T = 1
price_paths = []


for i in range(0, paths):
    price_paths.append(GeometricBrownianMotion(initial_price, drift, volatility, dt, T).prices)

call_payoffs = []
EC = European_Call_Payoff(100)
risk_free_rate = .01

for price_path in price_paths:
    call_payoffs.append(EC.get_payoff(price_path[-1])/(1 + risk_free_rate))  


plt.plot(price_path)   
plt.show()

print(np.average(call_payoffs)*100)  

```

![alt text](https://www.zupimages.net/up/22/04/sibi.png)



