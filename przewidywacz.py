# py -m pip install flask pandas numpy matplotlib statsmodels yfinance

from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
import yfinance as yf
from datetime import datetime, timedelta
import io
import base64

app = Flask(__name__)

# Function to fetch stock data from Yahoo Finance API
def fetch_stock_data(symbol, start_year):
    start_date = f"{start_year}-01-01"
    end_date = datetime.today().strftime('%Y-%m-%d')
    
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    stock_data = stock_data[['Adj Close']]
    stock_data.reset_index(inplace=True)
    stock_data.rename(columns={'Adj Close': 'adjusted_close'}, inplace=True)
    
    return stock_data.set_index('Date')

# Function to forecast stock prices using Winters or SARIMA model
def forecast_stock_prices(symbol, start_year, model_type):
    stock_data = fetch_stock_data(symbol, start_year)
    
    if model_type == 'Winters':
        model = ExponentialSmoothing(stock_data['adjusted_close'], seasonal='add', seasonal_periods=12)
    elif model_type == 'SARIMA':
        model = SARIMAX(stock_data['adjusted_close'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    elif model_type == 'ARIMA':
        model = ARIMA(stock_data['adjusted_close'], order=(5, 1, 0))
    elif model_type == 'Seasonal Naive':
        seasonal_naive_forecast = stock_data['adjusted_close'].shift(12)  # Shift by 12 months for seasonal naive
        last_seasonal_value = stock_data.iloc[-12]['adjusted_close']
        forecast = seasonal_naive_forecast.copy()
        for i in range(1, 31):  # Forecasting 30 days ahead
            forecast.iloc[-1 + i] = forecast.iloc[-12 + i] + (forecast.iloc[-12 + i] - last_seasonal_value)
        forecast_df = pd.DataFrame({'Date': stock_data.index[-1] + pd.to_timedelta(np.arange(1, 31), unit='D'), 'Forecast': forecast[-30:]})
        return stock_data, forecast_df.set_index('Date')
    else:
        raise ValueError("Invalid model type. Choose 'Winters' or 'SARIMA'.")
    
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=30)
    forecast_dates = [stock_data.index[-1] + timedelta(days=i+1) for i in range(30)]
    forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecast': forecast})
    forecast_df.set_index('Date', inplace=True)
    
    return stock_data, forecast_df

# Function to generate plot
def plot_forecast(stock_data, forecast_df, symbol):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(stock_data.index, stock_data['adjusted_close'], label='Historical Data')
    ax.plot(forecast_df.index, forecast_df['Forecast'], label='Forecast', linestyle='--', color='r')
    ax.set_title(f'Stock Price Forecast for {symbol}')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    ax.legend()
    ax.grid(True)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close(fig)
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    
    return plot_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forecast', methods=['POST'])
def forecast():
    try:
        symbol = request.form['symbol'].upper()
        start_year = int(request.form['year'])
        model_choice = request.form['model']
        
        historical_data, forecast_data = forecast_stock_prices(symbol, start_year, model_choice)
        plot_url = plot_forecast(historical_data, forecast_data, symbol)
        
        forecast_table = forecast_data.reset_index().to_dict(orient='records')
        
        return render_template('result.html', plot_url=plot_url, forecast_table=forecast_table, symbol=symbol)
    
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

@app.route('/description')
def description():
    return render_template('description.html')

if __name__ == '__main__':
    app.run(debug=True)
