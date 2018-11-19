import json
import numpy as np
import os
import pandas as pd
import urllib3
import h5py


# connect to poloniex's API
url = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1356998100&end=9999999999&period=300'
http = urllib3.PoolManager()

# parse json returned from the API to Pandas DF
openUrl = http.request('GET', url)
r = openUrl.data
d = json.loads(r.decode())
df = pd.DataFrame(d)

original_columns=[u'close', u'date', u'high', u'low', u'open']
new_columns = ['Close','Timestamp','High','Low','Open']
df = df.loc[:,original_columns]
df.columns = new_columns
df.head()

df['Datetime'] = pd.to_datetime('Timestamp')
df.head()

df.to_csv('data/bitcoin2015to2017.csv',index=None)
