import pandas as pd

def load_csv_data(data):
    """
    Loads stock data from a local CSV file
    """

    df = pd.read_csv('data.csv')

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'],utc = True)

    # Set Date as index
    df.set_index('Date', inplace=True)

    # Keep only Close price
    df = df[['Close']]

    # Remove missing values
    df.dropna(inplace=True)

    return df
