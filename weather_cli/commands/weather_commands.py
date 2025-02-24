import click
from ..services.location_service import ZippopotamLocationService
from ..services.weather_service import OpenMeteoWeatherService

location_service = ZippopotamLocationService()
weather_service = OpenMeteoWeatherService()

def where_is_command(zipcode: str = None) -> None:
    """Show the city and state for a location"""
    if zipcode:
        location = location_service.get_location_from_zip(zipcode)
        if location:
            click.echo(f"{zipcode} is in {location['city']}, {location['state']}")
        else:
            click.echo("Could not find location for that ZIP code")
    else:
        location = location_service.get_current_location()
        if location:
            click.echo(f"You are in {location['city']}, {location['state']}")
        else:
            click.echo("Could not determine current location")

def current_weather_command(zipcode: str = None) -> None:
    """Show current weather conditions"""
    if zipcode:
        location = location_service.get_location_from_zip(zipcode)
    else:
        location = location_service.get_current_location()
    
    if location:
        temp, conditions = weather_service.get_weather(location['lat'], location['lon'])
        if temp is not None:
            click.echo(f"It is currently {temp}ºF, and {conditions} in {location['city']}, {location['state']}")
        else:
            click.echo("Could not retrieve weather data")
    else:
        click.echo("Could not determine location")