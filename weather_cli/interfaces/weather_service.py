from abc import ABC, abstractmethod
from typing import Optional, Tuple

class WeatherService(ABC):
    @abstractmethod
    def get_weather(self, lat: str, lon: str) -> Tuple[Optional[float], Optional[str]]:
        """Get weather information for a location."""
        pass