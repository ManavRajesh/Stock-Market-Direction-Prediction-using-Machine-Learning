# Stock Market Direction Prediction using Machine Learning

This project predicts the **next-day direction of a stock price (up or down)** using machine learning techniques. Historical stock price data is transformed into technical indicators, and classification models are trained to identify patterns that indicate future price movement.

---

##  Project Overview

Stock market prediction is challenging due to the volatile and noisy nature of financial time-series data. Instead of predicting exact prices, this project focuses on **direction prediction**, which is more stable and widely used in financial research.

Using historical daily closing prices, various technical indicators are extracted and used as input features for machine learning models. The models classify whether the stock price is likely to increase or decrease on the following trading day.

---

##  Models Used

- **Linear Support Vector Machine (SVM)**
- **Logistic Regression**

Linear SVM is used for its efficiency and ability to handle high-dimensional feature spaces, while Logistic Regression serves as a baseline comparison model.

---

##  Features Used

The following features are derived from historical price data:

- Average return volatility
- Standard deviation (true) volatility
- Momentum
- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- Moving Average Convergence Divergence (MACD)

These features capture trend, momentum, and risk characteristics of the stock price.

---

## Prediction Target

For each trading day, the model predicts:

- **1** → Stock price will go **up** the next day  
- **0** → Stock price will go **down or remain unchanged**

This formulation treats the problem as a **binary classification task**.

---

##  Evaluation

Model performance is evaluated using:

- **Classification accuracy**
- **Visual analysis of predicted buy signals**
- **Simulated trading strategy**

The trading simulation demonstrates the practical usefulness of the predictions by measuring capital growth over time.

---

## 🗂 Project Structure

