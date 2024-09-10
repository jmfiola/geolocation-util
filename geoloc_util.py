import requests
import argparse
import json

BASE_URL = 'http://api.openweathermap.org/geo/1.0/'
COUNTRY_CODE = 'US'

def fetch_coordinates(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    return None

def get_coordinates_by_city_state(city_state, api_key):
    url = f"{BASE_URL}direct?q={city_state},{COUNTRY_CODE}&limit=1&appid={api_key}"
    data = fetch_coordinates(url)
    if data:
        return {
            'latitude': data[0]['lat'],
            'longitude': data[0]['lon'],
            'place_name': f"{data[0]['name']}, {data[0]['state']}, {data[0]['country']}"
        }
    return None

def get_coordinates_by_zip(zip_code, api_key):
    url = f"{BASE_URL}zip?zip={zip_code},{COUNTRY_CODE}&appid={api_key}"
    data = fetch_coordinates(url)
    if data:
        return {
            'latitude': data['lat'],
            'longitude': data['lon'],
            'place_name': f"{data['name']}, {data['country']}"
        }
    return None

def get_coordinates(location, api_key):
    if ',' in location:
        return get_coordinates_by_city_state(location, api_key)
    else:
        return get_coordinates_by_zip(location, api_key)

def main(locations, api_key):
    results = []
    for location in locations:
        result = get_coordinates(location, api_key)
        if result:
            results.append(result)
        else:
            results.append({'error': f"Could not find coordinates for {location}"})
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get coordinates for locations.")
    parser.add_argument('locations', nargs='+', help="List of locations (city, state or zip code)")
    parser.add_argument('--api-key', required=True, help="API key for OpenWeatherMap")
    args = parser.parse_args()
    main(args.locations, args.api_key)