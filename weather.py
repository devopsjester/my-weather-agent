import click
import requests
import geocoder
import json

def get_location_from_zip(zipcode):
    response = requests.get(f'https://api.zippopotam.us/us/{zipcode}')
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['places'][0]['place name'],
            'state': data['places'][0]['state'],
            'lat': data['places'][0]['latitude'],
            'lon': data['places'][0]['longitude']
        }
    return None

def get_current_location():
    g = geocoder.ip('me')
    if g.ok:
        return {
            'city': g.city,
            'state': g.state,
            'lat': g.lat,
            'lon': g.lng
        }
    return None

def get_weather(lat, lon):
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code&temperature_unit=fahrenheit')
    if response.status_code == 200:
        data = response.json()
        temp = data['current']['temperature_2m']
        weather_code = data['current']['weather_code']
        return temp, get_weather_description(weather_code)
    return None, None

def get_weather_description(code):
    weather_codes = {
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
    return weather_codes.get(code, "unknown conditions")

@click.group()
def cli():
    """Weather CLI application"""
    pass

@cli.command()
@click.option('--zipcode', help='ZIP code to look up')
def where_is(zipcode):
    """Show the city and state for a location"""
    if zipcode:
        location = get_location_from_zip(zipcode)
        if location:
            click.echo(f"{zipcode} is in {location['city']}, {location['state']}")
        else:
            click.echo("Could not find location for that ZIP code")
    else:
        location = get_current_location()
        if location:
            click.echo(f"You are in {location['city']}, {location['state']}")
        else:
            click.echo("Could not determine current location")

@cli.command()
@click.option('--zipcode', help='ZIP code to look up weather for')
def current(zipcode):
    """Show current weather conditions"""
    if zipcode:
        location = get_location_from_zip(zipcode)
    else:
        location = get_current_location()
    
    if location:
        temp, conditions = get_weather(location['lat'], location['lon'])
        if temp is not None:
            click.echo(f"It is currently {temp}ºF, and {conditions} in {location['city']}, {location['state']}")
        else:
            click.echo("Could not retrieve weather data")
    else:
        click.echo("Could not determine location")

if __name__ == '__main__':
    cli()