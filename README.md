# Weather Alert Bot 🌧️

## Receive automated WhatsApp notifications when rain is expected.

A Python application that retrieves hourly weather forecasts from WeatherAPI and automatically sends WhatsApp notifications when rain is expected during the day.

This project was built as part of a Data Engineering portfolio to demonstrate API integration, data processing, cloud deployment, and task automation using Python.

## Workflow

```mermaid
flowchart LR

A["WeatherAPI"] --> B["weather.py"]
B --> C["extract_forecast()"]
C --> D["Pandas DataFrame"]
D --> E["formatter.py"]
E --> F["notifier.py"]
F --> G["Twilio API"]
G --> H["WhatsApp"]
```

## Requirements

- Python 3.10+
- Twilio account
- WeatherAPI account

## Architecture

- **weather.py** → Retrieves weather data from WeatherAPI.
- **formatter.py** → Formats the weather forecast into a WhatsApp-friendly message.
- **notifier.py** → Sends notifications through the Twilio WhatsApp API.
- **main.py** → Coordinates the application workflow.
- **run.sh** → Entry point used for automated execution on Linux servers.

## Features

- Retrieves hourly forecasts from WeatherAPI
- Filters rain events between configurable hours
- Sends WhatsApp notifications using Twilio
- Uses environment variables for API credentials
- Modular project structure
- Basic HTTP error handling

## Technologies

- Python 3
- Requests
- Pandas
- Twilio SDK
- WeatherAPI

## Project Structure

```text
project_01_weather/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── run.sh
│
├── notebook/
│   └── Messages_Twilio.ipynb
│
├── src/
│   ├── main.py
│   ├── weather.py
│   ├── formatter.py
│   └── notifier.py
```

## Installation

Clone the repository

```bash
git clone https://github.com/IngDavidHoyosGil/weather-alert-bot.git
```

**Ubuntu/Debian:** if `venv` is not installed:

```bash
sudo apt install python3-venv
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file using `.env.example`.

Required variables:

```text
API_KEY_WAPI=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
PRIVATE_NUMBER=
```

## Run

Edit the target city in `src/main.py`:

```python
query = "London"
```

Then execute:

```bash
python -m src.main
```

## Example Output

### Rain expected

<p align="center">
  <img src="images/whatsapp_message.jpg" width="320">
</p>

### No rain expected

<p align="center">
    <img src="images/terminal_no_rain.png" width="700">
</p>

## Deployment

The application has been successfully deployed and tested on an AWS EC2 Ubuntu instance.

Typical deployment steps:

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies.
4. Configure the `.env` file.
5. Execute `run.sh`.

```bash
./run.sh
```

## Automation

The application can be scheduled using Linux cron.

Example:

```cron
0 10 * * * /home/ubuntu/weather-alert-bot/run.sh >> /home/ubuntu/weather-alert-bot/cron.log 2>&1
```

This schedules the application to run daily and stores execution logs in `cron.log`. Adjust the schedule according to your local timezone and deployment environment.

## Notes

This project uses the Twilio WhatsApp Sandbox.

Before running the application:

1. Open the Twilio Console.
2. Navigate to **Messaging → Try it out → Send a WhatsApp message**.
3. Follow the instructions to join the sandbox by sending the provided code from your WhatsApp account.
4. Once joined, run the application normally.

The Twilio WhatsApp Sandbox session expires periodically. If it expires, simply repeat the join process before running the application again.

## Future Improvements

- Support multiple cities
- Docker support
- Unit tests
- GitHub Actions CI
- Configurable execution schedule
- Replace the Twilio Sandbox with a production WhatsApp Business sender

## Roadmap

- [x] Consume WeatherAPI
- [x] Process hourly forecast
- [x] Send WhatsApp notifications
- [x] Deploy on AWS EC2
- [x] Automate with cron
- [ ] Containerize with Docker