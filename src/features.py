import numpy as np
from src.indicators import SMA, EMA, RSI, MACD

def build_features(stock, window=5):
    df = stock.copy()
    df.columns = ['Close']

    # Daily returns
    ret = df['Close'].pct_change()

    # Paper volatility (average return)
    df['vol_avg'] = ret.rolling(window).mean()

    # Improved volatility (std deviation)
    df['vol_std'] = ret.rolling(window).std()

    # Momentum
    df['momentum'] = np.sign(ret).rolling(window).mean()

    # Technical indicators
    df['SMA'] = SMA(df['Close'], 10)
    df['EMA'] = EMA(df['Close'], 10)
    df['RSI'] = RSI(df['Close'])
    df['MACD'] = MACD(df['Close'])

    # Target: next-day direction
    df['target'] = (df['Close'].shift(-1) > df['Close']).astype(int)

    df.dropna(inplace=True)

    X = df.drop(columns=['Close', 'target'])
    y = df['target']

    return X, y, df
