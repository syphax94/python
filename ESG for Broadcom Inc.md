### Broadcom Corporation

Est une entreprise américaine de l'industrie de l'électronique, qui développe des semi-conducteurs utilisés dans divers équipements de télécommunications. 

### Produits
- Solutions complètes de système sur puce unique (SoC) utilisables par divers équipementiers en télécommunications
- Semi-conducteurs intervenant dans la fabrication d'équipements de réseaux voix sur IP, notamment passerelles média, passerelles domestiques, boîtiers MTA pour les réseaux de câblo-distribution, adaptateurs de terminaux et terminaux téléphoniques IP.
- Position de leader sur le marché des semi-conducteurs pour les équipements de réseau Gigabit Ethernet.
- Circuits pour les applications d'encodage vidéo numérique haute définition aux formats H.264, MPEG2 HD et VC-1.
- Circuits pour les interfaces radio (Wi-Fi, FM, Bluetooth, GSM, CDMA…) intégrables dans des téléphones portables et autres appareils nomades.
- Circuits pour la localisation par satellite GPS.

### Code python
```python
import pandas as pd
import numpy as np
import yfinance as yf

broadcom = yf.Ticker("AVGO")

broadcom.info

main_df = pd.DataFrame()

broadcom_df = pd.DataFrame.from_dict(broadcom.info.items()).T
broadcom_df.columns = broadcom_df.iloc[0]
broadcom_df = broadcom_df.drop(broadcom_df.index[0])
main_df = main_df.append(broadcom_df)
print(f'{broadcom} + Complete')

dashboard = main_df[['symbol', 'sector','industry', 'previousClose', 'open','priceToBook','beta','ebitdaMargins','profitMargins', 'returnOnEquity','recommendationKey']]
dashboard.head(1) 

esg_df = broadcom.sustainability.T
esg_df

esg_data = esg_df[['socialScore','governanceScore', 'environmentScore', 'totalEsg']]
esg_data.head()

broadcom.major_holders

broadcom.institutional_holders

broadcom.recommendations

broadcom.dividends

import matplotlib.pyplot as plt

maximum_dividend = broadcom.dividends.max()
print('Maximum dividend is:',maximum_dividend,'%')

plt.figure(figsize=(12,8))
plt.plot(broadcom.dividends ,color='black')
plt.axhline(maximum_dividend, linestyle='--' , alpha = 0.5, color='red',label='Maximum dividend: 4.1 %')
plt.title('Dividend History for Broadcom Inc',fontsize=20)
plt.xlabel('Time Horizon', fontsize=17)
plt.ylabel('Dividends (%)', fontsize=17)
plt.legend()
plt.show()

```
### Ratio
![alt text](https://www.zupimages.net/up/22/11/zyza.png)

### ESG
![alt text](https://www.zupimages.net/up/22/11/8cfj.png)

### Actionnaires
![alt text](https://www.zupimages.net/up/22/11/hfqc.png)

### Recommandation
![alt text](https://www.zupimages.net/up/22/11/uj0g.png)

### Dividende croissant pour l'action Broadcom Inc
![alt text](https://www.zupimages.net/up/22/11/4c52.png)
