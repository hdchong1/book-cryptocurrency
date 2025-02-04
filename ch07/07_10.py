import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.8
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     # df['close'] / df['target'],
                     1)

ror = df['ror'].cumprod()[-2]
print(ror)

