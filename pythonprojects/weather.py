import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return weather, temperature, humidity, wind_speed
    else:
        print(f"Error: {data['message']}")
        return None, None, None, None

def main():
    api_key = "a2d761fc89e2ba58e4b1182023ea629d"  # Replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap
    cities = ["Barcelona", "New York", "Tokyo", "Paris", "Sydney", "Faisalabad", "Skardu", "Baltimore"]
    
    print("Weather Report for Different Cities:")
    print("-----------------------------------")
    for city in cities:
        weather, temperature, humidity, wind_speed = get_weather(api_key, city)
        if weather:
            print(f"City: {city}")
            print(f"Weather: {weather.capitalize()}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            print("-----------------------------------")
        else:
            print(f"Failed to fetch weather for {city}")

if __name__ == "__main__":
    main()
