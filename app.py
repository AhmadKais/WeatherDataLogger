import plotly
from flask import Flask, render_template, request, redirect, url_for
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.utils import PlotlyJSONEncoder
import json

app = Flask(__name__)

API_KEY = "5adbdb49da633f1f95e880a52e1ea962"
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

    current_data = current_weather_response.json()
    forecast_data = forecast_response.json()

    if current_weather_response.ok and forecast_response.ok:
        current_weather = {
            'city': city,
            'temperature': current_data['main']['temp'],
            'description': current_data['weather'][0]['description'],
            'humidity': current_data['main']['humidity'],
            'wind_speed': current_data['wind']['speed'],
            'icon': current_data['weather'][0]['icon']
        }

        # Process forecast data
        forecasts = []
        for item in forecast_data['list']:
            forecast = {
                'time': item['dt_txt'],
                'temp': item['main']['temp'],
                'description': item['weather'][0]['main']
            }
            forecasts.append(forecast)

        # Create plots
        forecast_df = pd.DataFrame(forecasts)
        temp_plot = create_temperature_plot(forecast_df)
        weather_plot_json = json.dumps(temp_plot, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('weather.html', weather=current_weather, forecasts=forecasts,
                               graphJSON=weather_plot_json)
    else:
        return f"Failed to retrieve weather data: {current_data.get('message', '')} {forecast_data.get('message', '')}"

def create_plot(df):
    fig = go.Figure(data=[go.Bar(x=df['city'], y=df['temperature'], text=df['temperature'], textposition='auto')])
    fig.update_layout(title_text='Current Temperature in °C')
    return fig

def create_temperature_plot(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['time'], y=df['temp'], mode='lines+markers', name='Temperature'))
    fig.update_layout(title='Temperature Forecast', xaxis_title='Time', yaxis_title='Temperature (°C)', template='plotly_dark')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
