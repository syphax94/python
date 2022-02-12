Interactive charts for Brent Crude Oil

```python
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

brent = yf.download('BZ=F', start="2009-01-01", end="2022-01-11")


area_chart = px.area(brent['Close'], title="Close Price")
area_chart.update_xaxes(
        title_text= 'Date',
        rangeslider_visible = True,
    rangeselector = dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])    
    
  )
)
area_chart.show()

```

![alt text](https://www.zupimages.net/up/22/06/ztpz.png)
