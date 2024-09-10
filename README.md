# Geolocation Utility

This utility fetches the latitude, longitude, and place name for given city/state or zip code inputs using the Open Weather Geocoding API. It supports multiple location inputs and returns the first result for each location.

## Features

- Fetches geolocation data (latitude, longitude, place name) for city/state or zip code inputs.
- Supports multiple location inputs in a single run.
- Utilizes the Open Weather Geocoding API for accurate and up-to-date information.

## Prerequisites

- Python 3.x installed on your machine.
- An API key from Open Weather Geocoding API. You can obtain one by signing up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

## Installation

1. Clone the repository:

    ```sh
    git clone git@github.com:jmfiola/geolocation-util.git
    cd geolocation-util
    ```

2. Install the required Python packages using `requirements.txt`
    ```sh
    python -m pip install -r requirements.txt
    ```

## Usage

Run the utility with a list of locations (city, state or zip code) and an API key:

```sh
python geoloc_util.py --api-key YOUR_API_KEY --locations "Madison, WI" "12345" "Chicago, IL" "10001"
```

This command will output the geolocation data for the specified locations.

## Testing

Run the integration tests using the following command:

```sh
python -m pytest test_geoloc_util.py --api-key YOUR_API_KEY
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.