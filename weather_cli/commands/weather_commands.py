import click
from ..services.location_service import ZippopotamLocationService
from ..services.weather_service import OpenMeteoWeatherService
from ..interfaces.location_service import LocationService
from ..interfaces.weather_service import WeatherService

class WeatherCommands:
    def __init__(
        self,
        location_service: LocationService = None,
        weather_service: WeatherService = None
    ):
        self.location_service = location_service or ZippopotamLocationService()
        self.weather_service = weather_service or OpenMeteoWeatherService()

    def where_is(self, zipcode: str = None) -> str:
        """Show the city and state for a location"""
        if zipcode:
            location = self.location_service.get_location_from_zip(zipcode)
            if location:
                return f"{zipcode} is in {location['city']}, {location['state']}"
            return "Could not find location for that ZIP code"
        else:
            location = self.location_service.get_current_location()
            if location:
                return f"You are in {location['city']}, {location['state']}"
            return "Could not determine current location"

    def current_weather(self, zipcode: str = None) -> str:
        """Show current weather conditions"""
        if zipcode:
            location = self.location_service.get_location_from_zip(zipcode)
        else:
            location = self.location_service.get_current_location()
        
        if location:
            temp, conditions = self.weather_service.get_weather(location['lat'], location['lon'])
            if temp is not None:
                return f"It is currently {temp}ºF, and {conditions} in {location['city']}, {location['state']}"
            return "Could not retrieve weather data"
        return "Could not determine location"

# Create default instance for CLI use
default_commands = WeatherCommands()

def where_is_command(zipcode: str = None) -> None:
    """CLI wrapper for where_is command"""
    click.echo(default_commands.where_is(zipcode))

def current_weather_command(zipcode: str = None) -> None:
    """CLI wrapper for current_weather command"""
    click.echo(default_commands.current_weather(zipcode))