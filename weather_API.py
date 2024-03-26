import requests

API_key = "c55ff4b020a2560045cad90bff5c6043"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")
# building url that includes city and API key as parameters
request_url = f"{BASE_URL}?appid={API_key}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    # grabbing weather and temp data from response
    weather = data['weather'][0]["description"]
    # converting temp from Kelvin to Celsius
    temperature = round(data['main']['temp'] - 273.15, 2)

    print("Weather: ", weather)
    print("Temperature: ", temperature, "Celsius")

else:
    print("An error occurred.")
