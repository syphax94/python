Assume we have a position in two credits:

p1= 0.001
p2= 0.004

And the joint probability of default over time horizon t is: 0.00018


```python
import numpy as np
import pandas as pd

def P(p12, p1, p2):
    px = (p12 -(p1*p2)) / ((np.sqrt(p1*(1-p1))) * (np.sqrt(p2*(1-p2))))
    return px
    
p1= 0.001
p2= 0.004
p12= 0.00018

px = P(p12, p1, p2) *100

print('The default correlation for this portfolio is: {0:.2f}'.format(px),'%')
```

![alt text](https://www.zupimages.net/up/22/05/jn9g.png)
