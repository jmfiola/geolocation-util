import subprocess
import json
import pytest

def run_geoloc_util(api_key, locations):
    result = subprocess.run(['python', 'geoloc_util.py', '--api-key', api_key] + locations, capture_output=True, text=True)
    return json.loads(result.stdout)

@pytest.mark.parametrize("locations, expected_place_names", [
    (["Madison, WI"], ["Madison, Wisconsin, US"]),
    (["12345"], ["Schenectady, US"]),
    (["Chicago, IL"], ["Chicago, Illinois, US"]),
    (["10001"], ["New York, US"]),
    (["Madison, WI", "12345", "Chicago, IL", "10001"], [
        "Madison, Wisconsin, US",
        "Schenectady, US",
        "Chicago, Illinois, US",
        "New York, US"
    ])
])
def test_locations(locations, expected_place_names, api_key):
    data = run_geoloc_util(api_key, locations)
    assert len(data) == len(expected_place_names)
    for i, expected_place_name in enumerate(expected_place_names):
        assert data[i]['place_name'] == expected_place_name
        assert 'latitude' in data[i]
        assert 'longitude' in data[i]
