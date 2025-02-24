import click
from .commands.weather_commands import where_is_command, current_weather_command

@click.group()
def cli():
    """Weather CLI application"""
    pass

@cli.command()
@click.option('--zipcode', help='ZIP code to look up')
def where_is(zipcode):
    """Show the city and state for a location"""
    where_is_command(zipcode)

@cli.command()
@click.option('--zipcode', help='ZIP code to look up weather for')
def current(zipcode):
    """Show current weather conditions"""
    current_weather_command(zipcode)