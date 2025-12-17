from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def evaluate(model, X_test, y_test, df_test):
    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)
    print("Accuracy:", acc)

    plt.figure(figsize=(10, 5))
    plt.plot(df_test['Close'], label='Actual Price')

    plt.scatter(
        df_test.index[pred == 1],
        df_test['Close'][pred == 1],
        color='green',
        marker='^',
        label='Predicted UP'
    )

    plt.legend()
    plt.grid()
    plt.show()
