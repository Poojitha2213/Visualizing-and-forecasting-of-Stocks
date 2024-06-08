import numpy as n
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data


start = '2010-01-01'
end = '2019-12-31'

df = data.DataReader('TSLA', 'yahoo', start, end, 3, 0.1, None, None)
df.head()
