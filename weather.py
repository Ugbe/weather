import requests

API_KEY = "80532158ef3c51b7377d75802928d76c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(f"Weather: {weather}")
    temperature = round(data['main']['temp'] - 273.15, 2)
    print(f"Temperature: {temperature}C")
else:
    print("An error occurred.")