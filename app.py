from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Make sure to replace this with your valid API key
API_KEY = "5adbdb49da633f1f95e880a52e1ea962"


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = {}
    if request.method == 'POST':
        city = request.form['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        print("URL requested:", url)  # Debug: Check the URL
        if response.ok:
            weather_data = response.json()
            print("Weather Data:", weather_data)  # Debug: Output received data
            weather = {
                'city': weather_data.get('name', 'City Not Found'),
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon']
            }
        else:
            print("Failed to fetch data:", response.status_code)  # Debug: API request failure
    return render_template('index.html', weather=weather)


if __name__ == '__main__':
    app.run(debug=True)
