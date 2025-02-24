import pytest
import responses
from weather_cli.services.location_service import ZippopotamLocationService

@pytest.fixture
def location_service():
    return ZippopotamLocationService()

@responses.activate
def test_get_location_from_zip_success(location_service):
    # Mock the Zippopotam API response
    responses.add(
        responses.GET,
        'https://api.zippopotam.us/us/90210',
        json={
            'places': [{
                'place name': 'Beverly Hills',
                'state': 'California',
                'latitude': '34.0901',
                'longitude': '-118.4065'
            }]
        },
        status=200
    )
    
    location = location_service.get_location_from_zip('90210')
    assert location['city'] == 'Beverly Hills'
    assert location['state'] == 'California'
    assert location['lat'] == '34.0901'
    assert location['lon'] == '-118.4065'

@responses.activate
def test_get_location_from_zip_not_found(location_service):
    # Mock API error response
    responses.add(
        responses.GET,
        'https://api.zippopotam.us/us/00000',
        status=404
    )
    
    location = location_service.get_location_from_zip('00000')
    assert location is None

def test_get_current_location_success(location_service, mocker):
    # Mock geocoder.ip response
    mock_ip = mocker.MagicMock()
    mock_ip.ok = True
    mock_ip.city = 'Rockville'
    mock_ip.state = 'Maryland'
    mock_ip.lat = 39.0840
    mock_ip.lng = -77.1528
    
    mocker.patch('geocoder.ip', return_value=mock_ip)
    
    location = location_service.get_current_location()
    assert location['city'] == 'Rockville'
    assert location['state'] == 'Maryland'
    assert location['lat'] == '39.084'
    assert location['lon'] == '-77.1528'

def test_get_current_location_failure(location_service, mocker):
    # Mock geocoder.ip failure
    mock_ip = mocker.MagicMock()
    mock_ip.ok = False
    
    mocker.patch('geocoder.ip', return_value=mock_ip)
    
    location = location_service.get_current_location()
    assert location is None