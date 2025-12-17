import pandas as pd
import numpy as np

def SMA(series, n):
    return series.rolling(n).mean()

def EMA(series, n):
    return series.ewm(span=n, adjust=False).mean()

def RSI(series, n=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    rs = gain.rolling(n).mean() / loss.rolling(n).mean()
    return 100 - (100 / (1 + rs))

def MACD(series):
    return EMA(series, 12) - EMA(series, 26)
