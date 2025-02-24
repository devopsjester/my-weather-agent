from abc import ABC, abstractmethod
from typing import Optional, TypedDict

class Location(TypedDict):
    city: str
    state: str
    lat: str
    lon: str

class LocationService(ABC):
    @abstractmethod
    def get_location_from_zip(self, zipcode: str) -> Optional[Location]:
        """Get location information from ZIP code."""
        pass

    @abstractmethod
    def get_current_location(self) -> Optional[Location]:
        """Get current location information."""
        pass