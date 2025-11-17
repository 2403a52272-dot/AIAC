import requests
from typing import Dict, Any

# task4.py
# Simple weather lookup using wttr.in (no API key required)
# Function accepts a city name, calls the API dynamically, and raises ValueError for invalid cities.



def get_weather(city: str, timeout: float = 5.0) -> Dict[str, Any]:
    """
    Fetch current weather for the given city using wttr.in (JSON).
    Raises ValueError if the city is invalid or network/response errors occur.

    Returns a dict with keys: city, temperature_C, feels_like_C, description, raw (original JSON).
    """
    if not city or not city.strip():
        raise ValueError("City name must not be empty")

    url = f"https://wttr.in/{requests.utils.requote_uri(city)}?format=j1"

    try:
        resp = requests.get(url, timeout=timeout, headers={"User-Agent": "weather-client/1.0"})
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        raise ValueError(f"Network error while contacting weather service: {e}")
    except ValueError:
        raise ValueError("Received invalid JSON from weather service")

    # Validate expected structure
    current = data.get("current_condition")
    if not current or not isinstance(current, list) or not current[0]:
        raise ValueError(f"Could not find weather for city: {city}")

    curr = current[0]
    temp_c = curr.get("temp_C")
    feels_like_c = curr.get("FeelsLikeC")

    # Extract human-readable description
    desc = ""
    wdesc = curr.get("weatherDesc")
    if isinstance(wdesc, list) and wdesc and isinstance(wdesc[0], dict):
        desc = wdesc[0].get("value", "")
    elif isinstance(wdesc, str):
        desc = wdesc

    # Try to get a normalized city name from the response (nearest_area)
    nearest_area = data.get("nearest_area")
    normalized_city = None
    if isinstance(nearest_area, list) and nearest_area and isinstance(nearest_area[0], dict):
        area_names = nearest_area[0].get("areaName")
        if isinstance(area_names, list) and area_names and isinstance(area_names[0], dict):
            normalized_city = area_names[0].get("value")

    return {
        "city": normalized_city or city,
        "temperature_C": int(temp_c) if temp_c and str(temp_c).lstrip("-").isdigit() else temp_c,
        "feels_like_C": int(feels_like_c) if feels_like_c and str(feels_like_c).lstrip("-").isdigit() else feels_like_c,
        "description": desc,
        "raw": data,
    }


if __name__ == "__main__":
    # small interactive demo
    try:
        city_input = input("Enter city name: ").strip()
        weather = get_weather(city_input)
        print(f"Weather for {weather['city']}: {weather['temperature_C']}°C, feels like {weather['feels_like_C']}°C, {weather['description']}")
    except ValueError as e:
        print(f"Error: {e}")