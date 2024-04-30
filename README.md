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
    - this command will run the program 
      - ```sh
        python app.py
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
    - if this does not work open the terminal and type `python app.py` then press enter
    - Wait for a few moments for the server to start.
    - Once the server is running, open a web browser and go to `http://127.0.0.1:5000/`.

3. **View Weather Data:**
    - Enter the name of the city you want to check the weather for.
    - Click on the `Check Weather` button.
    - You will see the current weather data along with a temperature forecast chart for the next 5 days and a prediction for the next 2 weeks.

4. **Stop the application:**
    - To stop the application, go back to PyCharm.
    - Press `Ctrl + C` in the terminal window where the Flask server is running.
### AWS Setup

1. **Install AWS CLI:**
    - Download and install AWS CLI from [here](https://aws.amazon.com/cli/).

2. **Configure AWS CLI:**
    - Open your terminal (Command Prompt on Windows).
    - Type the following command and press Enter:
        ```sh
        aws configure
        ```
    - Enter your AWS Access Key ID, AWS Secret Access Key, default region name, and default output format as prompted.
    - you get these from your AWS account manager i suggest using chatGPT for more precise instructions
    - even i got lost i cant help anymore i bearly understand what i did .
    - 
      Example:
      ```sh
      AWS Access Key ID [None]: *****************
      AWS Secret Access Key [None]: **********************
      Default region name [None]: eu-north-1
      Default output format [None]: json
      ```

3. **Create a DynamoDB Table:**
    - Open your terminal.
    - Type the following command and press Enter to create a DynamoDB table named "WeatherData":
      ```sh
      aws dynamodb create-table --table-name WeatherData --attribute-definitions AttributeName=city,AttributeType=S AttributeName=timestamp,AttributeType=N --key-schema AttributeName=city,KeyType=HASH AttributeName=timestamp,KeyType=RANGE --billing-mode PAY_PER_REQUEST
      ```
    - Wait for the table to be created.

4. **View DynamoDB Table:**
    - To view the data stored in your DynamoDB table:
        - Go to the [AWS Management Console](https://aws.amazon.com/console/).
        - Open the DynamoDB service.
        - Select the region where your table is located (in your case, "eu-north-1").
        - Click on the "Tables" link in the left navigation pane.
        - Click on your table name ("WeatherData") to view its details.
        - Click on the "Items" tab to view the data stored in your table.

## Support

If you have any questions or need assistance, please feel free to contact me at [ahmadqais1997@gmail.com].


