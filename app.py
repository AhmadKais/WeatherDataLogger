import plotly
from flask import Flask, render_template, request, redirect, url_for
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px
import json
from datetime import datetime, timedelta
import numpy as np
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

app = Flask(__name__)

API_KEY = "5adbdb49da633f1f95e880a52e1ea962"
DYNAMODB_REGION_NAME = "eu-north-1"
DYNAMODB_TABLE_NAME = "WeatherData"

dynamodb = boto3.resource('dynamodb', region_name=DYNAMODB_REGION_NAME)
table = dynamodb.Table(DYNAMODB_TABLE_NAME)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        return redirect(url_for('weather', city=city))
    return render_template('index.html')


@app.route('/weather/<city>')
def weather(city):
    current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'

    current_weather_response = requests.get(current_weather_url)
    forecast_response = requests.get(forecast_url)

    if current_weather_response.ok and forecast_response.ok:
        current_data = current_weather_response.json()
        forecast_data = forecast_response.json()

        current_weather = {
            'city': city,
            'temperature': Decimal(str(current_data['main']['temp'])),  # Convert to Decimal
            'description': current_data['weather'][0]['description'],
            'humidity': Decimal(str(current_data['main']['humidity'])),  # Convert to Decimal
            'wind_speed': Decimal(str(current_data['wind']['speed'])),  # Convert to Decimal
            'icon': current_data['weather'][0]['icon']
        }

        forecasts = [{
            'time': item['dt_txt'],
            'temp': Decimal(str(item['main']['temp'])),  # Convert to Decimal
            'description': item['weather'][0]['main']
        } for item in forecast_data['list']]

        forecast_df = pd.DataFrame(forecasts)
        five_day_plot = create_temperature_plot(forecast_df.head(40))  # Use only the first 5 days of 3-hourly forecasts

        extended_forecast_df, future_forecast_df = train_and_predict_temperature(forecast_df)
        two_week_plot = create_temperature_plot(future_forecast_df)  # ML predictions for the next two weeks

        # Convert plots to JSON for JavaScript in HTML
        five_day_plot_json = json.dumps(five_day_plot, cls=plotly.utils.PlotlyJSONEncoder)
        two_week_plot_json = json.dumps(two_week_plot, cls=plotly.utils.PlotlyJSONEncoder)

        # Save weather data to DynamoDB
        save_weather_data_to_dynamodb(current_weather)

        return render_template('weather.html', weather=current_weather,
                               graphJSON5Days=five_day_plot_json,
                               graphJSON2Weeks=two_week_plot_json)
    else:
        return "Failed to retrieve weather data."


def train_and_predict_temperature(df):
    df['timestamp'] = pd.to_datetime(df['time']).astype('int64') // 10 ** 9
    X = df[['timestamp']]
    y = df['temp']
    model = LinearRegression()
    model.fit(X, y)

    future_timestamps = np.array([df['timestamp'].iloc[-1] + 3 * 3600 * i for i in range(1, 337)]).reshape(-1, 1)
    future_temps = model.predict(future_timestamps)
    future_df = pd.DataFrame({
        'time': [datetime.utcfromtimestamp(ts[0]).strftime('%Y-%m-%d %H:%M:%S') for ts in future_timestamps],
        'temp': future_temps
    })
    return df, future_df


def create_temperature_plot(df):
    fig = px.line(df, x='time', y='temp', title='Temperature Forecast',
                  labels={'time': 'Time', 'temp': 'Temperature (°C)'})
    return fig


def save_weather_data_to_dynamodb(weather_data):
    table.put_item(
        Item={
            'city': weather_data['city'],
            'temperature': str(weather_data['temperature']),
            'description': weather_data['description'],
            'humidity': weather_data['humidity'],
            'wind_speed': weather_data['wind_speed'],
            'icon': weather_data['icon']
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
