import requests
import json
from datetime import datetime

def get_weather_details(city_name, api_key="YOUR_API_KEY"):
    try:
        # OpenWeatherMap API base URL
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Parameters for the API request
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric"  # For temperature in Celsius
        }
        
        # Make API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Get weather data in JSON format
        weather_data = response.json()
        
        # Format the data for storage
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_data = f"\n\n=== Weather Data for {city_name} at {timestamp} ===\n"
        formatted_data += json.dumps(weather_data, indent=2)
        
        # Append data to file
        with open("weather_history.txt", "a") as file:
            file.write(formatted_data)
        
        # Display JSON output
        print("\nWeather Data:")
        print(json.dumps(weather_data, indent=2))
        
        return weather_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key from OpenWeatherMap
    API_KEY = "your_api_key_here"
    city = input("Enter city name: ")
    get_weather_details(city, API_KEY)