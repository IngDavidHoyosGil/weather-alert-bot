import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY_WAPI = os.getenv("API_KEY_WAPI")

def get_weather(query):
    url_weather = "https://api.weatherapi.com/v1/forecast.json"
    
    params = {
        "key": API_KEY_WAPI,
        "q": query,
        "days": 1,
        "aqi": "no",
        "alerts": "no"
    }

    response = requests.get(
        url_weather,
        params = params,
        timeout = 10
    )

    response.raise_for_status()

    return response.json()

    
def extract_forecast(response):
    data = []

    for forecast in response["forecast"]["forecastday"][0]["hour"]:
        
        date = forecast['time'].split()[0]
        hour = int(forecast['time'].split()[1].split(':')[0])
        condition = forecast['condition']['text']
        temperature_c = forecast['temp_c']
        will_it_rain = forecast['will_it_rain'] 
        chance_of_rain = forecast['chance_of_rain'] 

        data.append(
            (date, hour, condition, temperature_c, will_it_rain, chance_of_rain)
        )

    return data




