import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)
print(df)

ror = df['ror'].cumprod()[-2]
ror1 = df['ror'].cumprod()
print(ror)
print(ror1)
