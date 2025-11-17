import sys
import json
import argparse

#!/usr/bin/env python3

def extract_fields(data):
    city = data.get("name") or data.get("city") or (data.get("location") or {}).get("name") or "Unknown"

    # temperature lookup
    temp = None
    if isinstance(data.get("main"), dict) and "temp" in data["main"]:
        temp = data["main"]["temp"]
    elif "temp" in data:
        temp = data["temp"]

    # humidity lookup
    humidity = None
    if isinstance(data.get("main"), dict) and "humidity" in data["main"]:
        humidity = data["main"]["humidity"]
    elif "humidity" in data:
        humidity = data["humidity"]

    # description lookup
    description = None
    w = data.get("weather")
    if isinstance(w, list) and w:
        description = w[0].get("description")
    elif isinstance(w, dict):
        description = w.get("description")
    description = description or data.get("description") or "N/A"

    # Convert temperature to Celsius if value looks like Kelvin (> 80)
    temp_c = None
    if temp is not None:
        try:
            t = float(temp)
            if t > 80:  # likely Kelvin
                temp_c = t - 273.15
            else:
                temp_c = t  # already Celsius (or Fahrenheit but we assume Celsius)
        except Exception:
            temp_c = None

    return city, temp_c, humidity, description

def print_friendly(city, temp_c, humidity, description):
    desc = str(description).capitalize()
    temp_str = f"{round(temp_c)}°C" if temp_c is not None else "N/A"
    humidity_str = f"{humidity}%" if humidity is not None else "N/A"

    print(f"• City: {city}")
    print(f"• Temperature: {temp_str}")
    print(f"• Humidity: {humidity_str}")
    print(f"Weather: {desc}")

def main():
    parser = argparse.ArgumentParser(description="Extract and print friendly weather info from API JSON.")
    parser.add_argument("file", nargs="?", help="Path to JSON file (omit to read from stdin).")
    args = parser.parse_args()

    raw = None
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            raw = f.read()
    else:
        if not sys.stdin.isatty():
            raw = sys.stdin.read()

    if raw:
        data = json.loads(raw)
    else:
        # fallback sample (runs even with no input)
        data = {
            "name": "London",
            "main": {"temp": 291.15, "humidity": 60},
            "weather": [{"description": "clear sky"}]
        }

    city, temp_c, humidity, description = extract_fields(data)
    print_friendly(city, temp_c, humidity, description)

if __name__ == "__main__":
    main()