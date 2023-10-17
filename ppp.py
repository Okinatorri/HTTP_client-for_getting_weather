import requests

def get_weather(city):
    api_key = "6802be0f69dbe16900b8c390d1cffdb5"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    city = input("Введите название города: ")
    weather_data = get_weather(city)
    print(f"Погода в городе {city}:")
    print(weather_data)
