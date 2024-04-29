# Weather App

This is a simple weather forecasting web application built with Python Flask, Plotly for data visualization, and OpenWeatherMap API for weather data.

## Getting Started

### Prerequisites

- PyCharm (Any IDE that supports Python)
- Python 3.x installed on your system
- Basic knowledge of using a command-line interface (Terminal on macOS/Linux, Command Prompt or PowerShell on Windows)

### Installation

1. **Clone the repository:**
    - Open your terminal (Command Prompt on Windows).
    - Change the current working directory to the location where you want the cloned directory.
    - Type the following command and press Enter:
        ```
        git clone https://github.com/AhmadKais/WeatherDataLogger
        ```
        
2. **Install dependencies:**
    - Open PyCharm.
    - Open the project folder `WeatherDataLogger`.
    - Open a terminal inside PyCharm:
        - Click on `View` from the top menu.
        - Select `Tool Windows`.
        - Click on `Terminal`.
        - or you can pres `Alt + f12`
    - In the terminal, type the following command and press Enter:
      this command will change the directory the requirements file dir :
      - ```sh
        cd WeatherDataLogger
        ```  
    - this command will install the required libraries 
      - ```sh
        pip install -r requirements.txt
        ```

### Usage

1. **Set up OpenWeatherMap API Key:**
    - Sign up on [OpenWeatherMap](https://openweathermap.org/) and get your API key.
    - Open the `app.py` file in the project.
    - Replace `YOUR_API_KEY` with your actual API key:
        ```python
        API_KEY = "YOUR_API_KEY"
        ```

2. **Run the application:**
    - In PyCharm, make sure the `app.py` file is open.
    - Right-click on `app.py` in the Project Explorer (on the left).
    - Choose `Run 'app'`.
    - Wait for a few moments for the server to start.
    - Once the server is running, open a web browser and go to `http://127.0.0.1:5000/`.

3. **View Weather Data:**
    - Enter the name of the city you want to check the weather for.
    - Click on the `Check Weather` button.
    - You will see the current weather data along with a temperature forecast chart for the next 5 days and a prediction for the next 2 weeks.

4. **Stop the application:**
    - To stop the application, go back to PyCharm.
    - Press `Ctrl + C` in the terminal window where the Flask server is running.

## Support

If you have any questions or need assistance, please feel free to contact me at [ahmadqais1997@gmail.com].

