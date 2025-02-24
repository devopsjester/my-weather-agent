import requests
from typing import Dict, Optional, Tuple
from ..interfaces.weather_service import WeatherService

class OpenMeteoWeatherService(WeatherService):
    def __init__(self):
        self._weather_codes: Dict[int, str] = {
            0: "clear sky",
            1: "mainly clear",
            2: "partly cloudy",
            3: "overcast",
            45: "foggy",
            48: "depositing rime fog",
            51: "light drizzle",
            53: "moderate drizzle",
            55: "dense drizzle",
            61: "slight rain",
            63: "moderate rain",
            65: "heavy rain",
            71: "slight snow fall",
            73: "moderate snow fall",
            75: "heavy snow fall",
            77: "snow grains",
            80: "slight rain showers",
            81: "moderate rain showers",
            82: "violent rain showers",
            85: "slight snow showers",
            86: "heavy snow showers",
            95: "thunderstorm"
        }

    def get_weather(self, lat: str, lon: str) -> Tuple[Optional[float], Optional[str]]:
        response = requests.get(
            f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}'
            f'&current=temperature_2m,weather_code&temperature_unit=fahrenheit'
        )
        if response.status_code == 200:
            data = response.json()
            temp = data['current']['temperature_2m']
            weather_code = data['current']['weather_code']
            return temp, self._weather_codes.get(weather_code, "unknown conditions")
        return None, None