import sys
import requests


def get_weather(city: str) -> dict:
    """Fetch raw weather data for a given city from wttr.in API."""
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("No internet connection. Please check your network.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
        sys.exit(1)
    except requests.exceptions.HTTPError:
        print(f"City '{city}' not found. Please check the spelling.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


def parse_weather(data: dict) -> dict:
    """Extract and return relevant weather fields from API response."""
    condition = data["current_condition"][0]
    nearest_area = data["nearest_area"][0]

    return {
        "city": nearest_area["areaName"][0]["value"],
        "country": nearest_area["country"][0]["value"],
        "temperature_c": condition["temp_C"],
        "temperature_f": condition["temp_F"],
        "feels_like_c": condition["FeelsLikeC"],
        "humidity": condition["humidity"],
        "wind_speed_kmph": condition["windspeedKmph"],
        "wind_direction": condition["winddir16Point"],
        "visibility_km": condition["visibility"],
        "uv_index": condition["uvIndex"],
        "description": condition["weatherDesc"][0]["value"],
    }