from src.data_loader import load_csv_data
from src.features import build_features
from src.models import get_models
from src.backtest import trading_simulation
from src.evaluation import evaluate

# Load data
stock = load_csv_data("data.csv")

# Feature engineering
X, y, df = build_features(stock)

# Train-test split (time series)
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]
df_test = df.iloc[split:]

models = get_models()

for name, model in models.items():
    print(f"\n===== {name} =====")

    model.fit(X_train, y_train)

    evaluate(model, X_test, y_test, df_test)

    final_capital = trading_simulation(
        df_test['Close'].values,
        model.predict(X_test)
    )

    print("Final Capital:", final_capital)
