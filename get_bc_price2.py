import os
import json
import numpy as np
import pandas as pd
import h5py
import requests
from datetime import datetime


# connect to poloniex's API
url = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1356998100&end=9999999999&period=300'

r = requests.get(url)
d = json.loads(r.text)
#print(d)

df = pd.DataFrame(d)
print(df.columns)
print(df.head())

original_columns=[u'close', u'date', u'high', u'low', u'open', u'quoteVolume', u'volume', u'weightedAverage']
new_columns = ['Close','Timestamp','High','Low','Open', 'quoteVolume', 'volume', 'weightedAverage']
df = df.loc[:,original_columns]
df.columns = new_columns

print(df.head())

df['Datetime'] = pd.to_datetime(df['Timestamp'],unit='s')
#print(df.tail(-10))
print(df.tail())

df.to_csv('data/bitcoin2.csv',index=None)
