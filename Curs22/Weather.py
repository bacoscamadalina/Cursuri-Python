'''
                                       Built-in API request by city name
'''
from datetime import datetime

import requests
from pprint import pprint


class OpenWeatherMap:
    URL_WEATHER = 'https://api.openweathermap.org/data/2.5/weather'
    API_KEY = '02722d8b0621f649ca69b7ce2e38c157'
    URL_FORECAST = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, city_name):
        self.city_name = city_name

    def get_weather_now(self):
        complete_url = f'{self.URL_WEATHER}?appid={self.API_KEY}&q={self.city_name}&units=metric'
        response = requests.get(complete_url)
        weather_data = response.json()
        #pprint(weather_data)
        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            print(f'Weather in {self.city_name} ')
            print(f'Temperature:  {temperature} ')
            print(f'Humidity: {humidity} ')
            print(f'Description: {description} ')
        else:
            print(f'Error : {weather_data.get("message","City not found")}')

    def get_wind_details(self):
        complete_url = f"{self.URL_WEATHER}appid={self.API_KEY}&q={self.city_name}&units=metric"
        response = requests.get(complete_url)

        if response.ok:
            weather_data = response.json()
            wind_speed = weather_data['wind']['speed']
            wind_deg = weather_data['wind']['deg']
            print(f"Detalii vânt pentru {self.city_name}:")
            print(f"Viteza vântului: {wind_speed} m/s")
            print(f"Direcția vântului: {wind_deg} grade")
            print(30 * "#")
        else:
            print("Error: City not found.")

    def get_forecast(self):
        complete_url = f"{self.URL_FORECAST}appid={self.API_KEY}&q={self.city_name}&units=metric"
        response = requests.get(complete_url)

        if response.ok:
            forecast_data = response.json()
            print(f"Prognoza meteo pe 5 zile pentru {self.city_name}:\n")
            for item in forecast_data['list']:
                date_time = datetime.utcfromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S')
                temperature = item['main']['temp']
                description = item['weather'][0]['description']
                print(f"Data și ora: {date_time}")
                print(f"Temperatura: {temperature}°C")
                print(f"Descrierea: {description}\n")
        else:
            print(f"Error: Unable to fetch forecast data.")


city_name = input("Enter city name: ")
weather_client = OpenWeatherMap(city_name)
weather_client.get_weather_now()
weather_client.get_wind_details()
weather_client.get_forecast()




