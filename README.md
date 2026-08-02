# 📈 CryptoVision ARIMA – Cryptocurrency Price Forecasting

CryptoVision ARIMA is a Machine Learning and Time Series Forecasting web application that predicts future cryptocurrency prices using the **ARIMA (AutoRegressive Integrated Moving Average)** model. 
The application is built with **Streamlit** and retrieves real-time cryptocurrency market data from **Yahoo Finance** to generate accurate short-term forecasts.

🌐 **Live Demo:** https://cryptovision-arima.onrender.com

---

## 📌 Features

- Real-time cryptocurrency data from Yahoo Finance
- Forecast future cryptocurrency prices using the ARIMA model
- Automatic ARIMA parameter selection based on minimum Mean Squared Error (MSE)
- Interactive Plotly visualization
- Adjustable forecast horizon (1–15 days)
- Displays latest market price and predicted future price
- Responsive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- ARIMA (Statsmodels)
- Scikit-learn
- Plotly
- Yahoo Finance (yfinance)
- Pillow (PIL)

---

## 📊 Supported Features

The application allows users to:

- Select a cryptocurrency
- Download the latest historical market data
- Train an ARIMA forecasting model
- Predict prices up to 30 days ahead
- Visualize:
  - Historical prices
  - Training data
  - Test predictions
  - Future forecasts

---

## 🤖 Forecasting Model

### Algorithm
**ARIMA (AutoRegressive Integrated Moving Average)**

The application automatically evaluates multiple combinations of:

- p (Auto Regression)
- d (Differencing)
- q (Moving Average)

The model with the **lowest Mean Squared Error (MSE)** is selected for forecasting.

---

## 📈 Dashboard Features

The dashboard includes:

- Cryptocurrency Selector
- Prediction Days Input
- Latest Closing Price
- Forecasted Future Price
- Interactive Plotly Forecast Graph
- Automatic Train/Test Split Visualization

---

## 📂 Project Structure

```
CryptoVision-ARIMA/
│
├── app.py
├── crypto_list.csv
├── Pic1.PNG
├── Pic2.PNG
├── requirements.txt
├── README.md

```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/CryptoVision-ARIMA.git
```

Navigate to the project folder

```bash
cd CryptoVision-ARIMA
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run car_predict.py
```

---

## 📋 Requirements

```
streamlit
pandas
numpy
statsmodels
scikit-learn
plotly
yfinance
matplotlib
Pillow
```

---

## 📊 How It Works

1. Select a cryptocurrency from the sidebar.
2. Choose the number of days to forecast (1-15).
3. Click **Predict**.
4. The application downloads recent market data from Yahoo Finance.
5. Multiple ARIMA models are evaluated automatically.
6. The model with the lowest Mean Squared Error (MSE) is selected.
7. Future cryptocurrency prices are forecast and displayed.
8. An interactive Plotly chart visualizes historical prices, train/test predictions, and future forecasts.

---

## 📷 Application Preview

The application includes:

- Responsive Streamlit interface
- Cryptocurrency selection panel
- Live price metrics
- Interactive forecasting dashboard
- Historical and future price visualization

<img width="1915" height="789" alt="crypto" src="https://github.com/user-attachments/assets/16f64732-6998-41a2-914d-876f894fbbe4" />


---

## 🌐 Live Application

**Render Deployment**

https://cryptovision-arima.onrender.com

---

## 🚀 Future Enhancements

- Support additional forecasting models (SARIMA, Prophet, LSTM)
- Confidence interval visualization
- Technical indicators integration (RSI, MACD, Bollinger Bands)
- Multi-cryptocurrency comparison
- Download forecast reports
- Historical forecast accuracy metrics
- Portfolio tracking dashboard

---

## 👩‍💻 Developed By

**Shrusti Diggavi**

IPEC Solutions Pvt Ltd, Bangalore

---

## 📄 License

This project is developed for educational, research, and portfolio purposes.
