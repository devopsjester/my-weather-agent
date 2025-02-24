import requests
import geocoder
from typing import Optional
from ..interfaces.location_service import LocationService, Location

class ZippopotamLocationService(LocationService):
    def get_location_from_zip(self, zipcode: str) -> Optional[Location]:
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

    def get_current_location(self) -> Optional[Location]:
        g = geocoder.ip('me')
        if g.ok:
            return {
                'city': g.city,
                'state': g.state,
                'lat': str(g.lat),
                'lon': str(g.lng)
            }
        return None