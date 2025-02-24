import pytest
from weather_cli.commands.weather_commands import WeatherCommands
from weather_cli.interfaces.location_service import LocationService, Location
from weather_cli.interfaces.weather_service import WeatherService
from typing import Optional, Tuple

class MockLocationService(LocationService):
    def __init__(self, mock_zip_location: Optional[Location] = None, mock_current_location: Optional[Location] = None):
        self.mock_zip_location = mock_zip_location
        self.mock_current_location = mock_current_location

    def get_location_from_zip(self, zipcode: str) -> Optional[Location]:
        return self.mock_zip_location

    def get_current_location(self) -> Optional[Location]:
        return self.mock_current_location

class MockWeatherService(WeatherService):
    def __init__(self, mock_temp: Optional[float] = None, mock_condition: Optional[str] = None):
        self.mock_temp = mock_temp
        self.mock_condition = mock_condition

    def get_weather(self, lat: str, lon: str) -> Tuple[Optional[float], Optional[str]]:
        return self.mock_temp, self.mock_condition

def test_where_is_with_zipcode_success():
    mock_location = {
        'city': 'Beverly Hills',
        'state': 'California',
        'lat': '34.0901',
        'lon': '-118.4065'
    }
    location_service = MockLocationService(mock_zip_location=mock_location)
    commands = WeatherCommands(location_service=location_service)
    
    result = commands.where_is(zipcode='90210')
    assert result == '90210 is in Beverly Hills, California'

def test_where_is_with_zipcode_not_found():
    location_service = MockLocationService(mock_zip_location=None)
    commands = WeatherCommands(location_service=location_service)
    
    result = commands.where_is(zipcode='00000')
    assert result == 'Could not find location for that ZIP code'

def test_where_is_current_location_success():
    mock_location = {
        'city': 'Rockville',
        'state': 'Maryland',
        'lat': '39.0840',
        'lon': '-77.1528'
    }
    location_service = MockLocationService(mock_current_location=mock_location)
    commands = WeatherCommands(location_service=location_service)
    
    result = commands.where_is()
    assert result == 'You are in Rockville, Maryland'

def test_where_is_current_location_failure():
    location_service = MockLocationService(mock_current_location=None)
    commands = WeatherCommands(location_service=location_service)
    
    result = commands.where_is()
    assert result == 'Could not determine current location'

def test_current_weather_success():
    mock_location = {
        'city': 'Beverly Hills',
        'state': 'California',
        'lat': '34.0901',
        'lon': '-118.4065'
    }
    location_service = MockLocationService(mock_zip_location=mock_location)
    weather_service = MockWeatherService(mock_temp=72.5, mock_condition='clear sky')
    commands = WeatherCommands(
        location_service=location_service,
        weather_service=weather_service
    )
    
    result = commands.current_weather(zipcode='90210')
    assert result == 'It is currently 72.5ºF, and clear sky in Beverly Hills, California'

def test_current_weather_location_not_found():
    location_service = MockLocationService(mock_zip_location=None)
    weather_service = MockWeatherService(mock_temp=72.5, mock_condition='clear sky')
    commands = WeatherCommands(
        location_service=location_service,
        weather_service=weather_service
    )
    
    result = commands.current_weather(zipcode='00000')
    assert result == 'Could not determine location'

def test_current_weather_api_failure():
    mock_location = {
        'city': 'Beverly Hills',
        'state': 'California',
        'lat': '34.0901',
        'lon': '-118.4065'
    }
    location_service = MockLocationService(mock_zip_location=mock_location)
    weather_service = MockWeatherService(mock_temp=None, mock_condition=None)
    commands = WeatherCommands(
        location_service=location_service,
        weather_service=weather_service
    )
    
    result = commands.current_weather(zipcode='90210')
    assert result == 'Could not retrieve weather data'