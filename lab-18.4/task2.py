import requests
import json
def get_weather_details(city, api_key):
    try:
        # OpenWeatherMap API endpoint
        base_url = "https://api.openweathermap.org/data/2.5/weather"

        # Parameters for the API request
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # For temperature in Celsius
        }

        # Make the API request
        response = requests.get(base_url, params=params)

        # Raise an exception for bad status codes
        response.raise_for_status()

        # Parse the JSON response
        weather_data = response.json()

        # Print formatted JSON output
        print(json.dumps(weather_data, indent=2))

        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Get inputs from user
    API_KEY = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")

    weather_data = get_weather_details(city, API_KEY)

    if weather_data is None:
        print("Failed to get weather data.")