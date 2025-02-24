# Weather CLI

A simple command-line weather application that shows current weather conditions using free, no-registration-required APIs.

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   # or
   .\venv\Scripts\activate  # On Windows
   ```
3. Install the package:
   ```bash
   pip install -e .
   ```

## Usage

The CLI provides two main commands:

### Check Location

Show city and state for a location:
```bash
weather where-is  # Shows your current location
weather where-is --zipcode 90210  # Shows location for a specific ZIP code
```

### Check Weather

Show current weather conditions:
```bash
weather current  # Shows weather for your current location
weather current --zipcode 90210  # Shows weather for a specific ZIP code
```

## APIs Used

- Location lookup: zippopotam.us (free, no API key required)
- Weather data: Open-Meteo (free, no API key required)
- IP Geolocation: ip-api.com (free, no API key required)