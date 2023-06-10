import requests
import json

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)
    print(weather_data)
    if weather_data.get("cod") == "404":
        print("City not found.")
        return
    
    # Extract relevant weather information
    temperature = weather_data.get("main", {}).get("temp")
    humidity = weather_data.get("main", {}).get("humidity")
    description = weather_data.get("weather", [{}])[0].get("description")
    
    # Display the weather information
    print(f"Weather in {city}:")
    if temperature:
        print(f"Temperature: {temperature}°C")
    if humidity:
        print(f"Humidity: {humidity}%")
    if description:
        print(f"Description: {description}")

# Enter your OpenWeatherMap API key here
api_key = "f0350b36185a1fdcf63be2b81d5de756"

# Enter the city for which you want to get weather information
city = input("Enter city name: ")

# Call the function to get the weather information
get_weather(city, api_key)
