import pandas as pd
import numpy as np
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from itertools import product
import warnings
import streamlit as st
from PIL import Image

warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")
st.markdown("<style>.main {padding-top: 0px;}</style>", unsafe_allow_html=True)

st.sidebar.image("Pic2.PNG", width="stretch")
st.image("Pic1.PNG", width="stretch")

st.markdown(
    "<h1 style='text-align: center; margin-top: -20px;'>ARIMA Forecasting Model</h1>",
    unsafe_allow_html=True
)

st.sidebar.header("Model Parameters")

crypto_df = pd.read_csv("crypto_list.csv")

selected_crypto = st.sidebar.selectbox(
    "Select Cryptocurrency",
    crypto_df["CoinName"]
)

crypto_symbol = (
    crypto_df.loc[
        crypto_df["CoinName"] == selected_crypto,
        "Symbol"
    ].iloc[0]
    + "-USD"
)

prediction_ahead = st.sidebar.number_input(
    "Prediction Days Ahead",
    min_value=1,
    max_value=30,
    value=15,
    step=1
)

if st.sidebar.button("Predict"):

    btc_data = yf.download(
        crypto_symbol,
        period="3mo",
        interval="1d",
        auto_adjust=True
    )

    # yfinance returns a MultiIndex on columns for single tickers in recent versions.
    # Flatten it so btc_data["Close"] is a plain Series, not a 1-column DataFrame.
    if isinstance(btc_data.columns, pd.MultiIndex):
        btc_data.columns = btc_data.columns.get_level_values(0)

    btc_data = btc_data[['Close']].dropna()

    if btc_data.empty:
        st.error("No Yahoo Finance data available for this cryptocurrency.")
        st.stop()

    train_size = int(len(btc_data) * 0.8)
    train = btc_data[:train_size]
    test = btc_data[train_size:]

    p_values = range(0, 4)
    d_values = range(0, 2)
    q_values = range(0, 4)

    def evaluate_arima_model(train, test, arima_order):
        try:
            model = ARIMA(train, order=arima_order)
            model_fit = model.fit()
            predictions = model_fit.forecast(steps=len(test))
            mse = mean_squared_error(test, predictions)
            return mse, model_fit
        except:
            return float("inf"), None

    results = []

    for p, d, q in product(p_values, d_values, q_values):

        order = (p, d, q)

        mse, model_fit = evaluate_arima_model(
            train["Close"],
            test["Close"],
            order
        )

        results.append((order, mse, model_fit))

    best_order, best_mse, best_model = min(
        results,
        key=lambda x: x[1]
    )

    forecast = best_model.forecast(
        steps=len(test) + prediction_ahead
    )

    latest_close_price = btc_data["Close"].iloc[-1]

    if isinstance(latest_close_price, pd.Series):
        latest_close_price = latest_close_price.iloc[0]

    latest_close_price = float(latest_close_price)

    last_predicted_price = forecast.iloc[-1]

    if isinstance(last_predicted_price, pd.Series):
        last_predicted_price = last_predicted_price.iloc[0]

    last_predicted_price = float(last_predicted_price)

    col1, col2 = st.columns(2)

    with col1:
    	st.metric(
           "Latest Close Price",
           f"${latest_close_price:,.2f}"
    	)

    with col2:
    	st.metric(
           f"Price After {prediction_ahead} Days",
           f"${last_predicted_price:,.2f}"
    	)

    import plotly.graph_objects as go

    

# Plot
    fig = go.Figure()

# Actual Price
    fig.add_trace(
        go.Scatter(
            x=btc_data.index,
            y=btc_data["Close"].values,
            mode="lines",
            name="Actual Price",
            line=dict(color="blue", width=2),
            hovertemplate="<b>Date:</b> %{x}<br><b>Price:</b> $%{y:,.2f}<extra></extra>"
        )
    )

# Train Data
    fig.add_trace(
        go.Scatter(
            x=train.index,
            y=train["Close"].values,
            mode="lines",
            name="Train Data",
            line=dict(color="green", width=2),
            hovertemplate="<b>Date:</b> %{x}<br><b>Price:</b> $%{y:,.2f}<extra></extra>"
        )
    )

# Test Prediction
    fig.add_trace(
        go.Scatter(
            x=test.index,
            y=forecast.iloc[:len(test)].values,
            mode="lines",
            name="Test Prediction",
            line=dict(color="orange", width=2),
            hovertemplate="<b>Date:</b> %{x}<br><b>Predicted:</b> $%{y:,.2f}<extra></extra>"
        )
    )

# Future Prediction
    future_index = pd.date_range(
        start=test.index[-1],
        periods=prediction_ahead + 1,
        freq="D"
    )[1:]

    fig.add_trace(
        go.Scatter(
            x=future_index,
            y=forecast.iloc[len(test):].values,
            mode="lines+markers",
            name=f"{prediction_ahead} Day Forecast",
            line=dict(color="red", width=3),
            hovertemplate="<b>Date:</b> %{x}<br><b>Forecast:</b> $%{y:,.2f}<extra></extra>"
        )
    )

# Train/Test Split
    fig.add_vline(
        x=btc_data.index[train_size],
        line_dash="dash",
        line_color="gray"
    )

    fig.update_layout(
        title=f"{selected_crypto} ARIMA Forecast",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        hovermode="x unified",
        template="plotly_dark",
        height=550
    )

    st.plotly_chart(fig, width="stretch")
st.markdown("---")
st.markdown(
    """
    <div style="
        text-align:center;
        padding:15px;
        border-radius:10px;
        background-color:#1f1f1f;
        color:white;
        font-size:16px;">
        <h4>Developed by</h4>
        <h3 style="color:#00D4FF;">Shrusti Diggavi</h3>
        <p>IPEC Solutions Pvt Ltd, Bangalore</p>
    </div>
    """,
    unsafe_allow_html=True
)