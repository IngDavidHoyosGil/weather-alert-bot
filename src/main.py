from src.weather import get_weather, extract_forecast
from src.formatter import build_message
from src.notifier import send_message
import pandas as pd
import requests
import sys

START_HOUR = 5
END_HOUR = 22

def main():
    query = "Buenaventura"

    try:
        response = get_weather(query)
    except requests.exceptions.HTTPError as e:
        print(f"WeatherAPI returned HTTP {e.response.status_code}.")
        sys.exit(1)

    except requests.exceptions.Timeout:
        print("WeatherAPI timed out.")
        sys.exit(1)
    
    except requests.exceptions.ConnectionError:
        print("Unable to connect to WeatherAPI.")
        sys.exit(1)
    
    except requests.exceptions.RequestException:
        print("Unexpected error while contacting WeatherAPI.")
        sys.exit(1)

    data = extract_forecast(response)
    
    columns = [
        'Date',
        'Hour',
        'Condition',
        'Temperature(C°)',
        'Will_it_rain',
        'Chance_of_rain'
    ]
    df = pd.DataFrame(data, columns = columns)
    date = df['Date'][0]
    
    df_rain = df[
        (df['Will_it_rain'] == 1) & 
        (df['Hour'].between(START_HOUR, END_HOUR))
        ][['Hour', 'Condition', 'Chance_of_rain']]
    
    message_string = build_message(df_rain, date, query)

    if df_rain.empty:
        print(f"No rain expected today in {query}. No message will be sent")
    else:
        send_message(message_string)

    print(f"\n{df}")

if __name__ == "__main__":
    main()

    