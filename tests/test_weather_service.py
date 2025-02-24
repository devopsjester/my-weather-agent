import pytest
import responses
from weather_cli.services.weather_service import OpenMeteoWeatherService

@pytest.fixture
def weather_service():
    return OpenMeteoWeatherService()

@responses.activate
def test_get_weather_success(weather_service):
    # Mock the API response
    responses.add(
        responses.GET,
        'https://api.open-meteo.com/v1/forecast',
        json={
            'current': {
                'temperature_2m': 72.5,
                'weather_code': 0
            }
        },
        status=200
    )
    
    temp, condition = weather_service.get_weather('34.0901', '-118.4065')
    assert temp == 72.5
    assert condition == 'clear sky'

@responses.activate
def test_get_weather_api_error(weather_service):
    # Mock API error response
    responses.add(
        responses.GET,
        'https://api.open-meteo.com/v1/forecast',
        status=500
    )
    
    temp, condition = weather_service.get_weather('34.0901', '-118.4065')
    assert temp is None
    assert condition is None

@responses.activate
def test_get_weather_unknown_condition(weather_service):
    # Mock response with unknown weather code
    responses.add(
        responses.GET,
        'https://api.open-meteo.com/v1/forecast',
        json={
            'current': {
                'temperature_2m': 72.5,
                'weather_code': 999  # Unknown code
            }
        },
        status=200
    )
    
    temp, condition = weather_service.get_weather('34.0901', '-118.4065')
    assert temp == 72.5
    assert condition == 'unknown conditions'