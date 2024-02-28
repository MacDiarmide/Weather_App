import requests

api_key = 'ad6e3d1262d3f8dc675a19aaa2ee7702'

while True:
    user_input = input('Введите название города: ')
    try:
        weather_data = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&lang=ru&appid={api_key}')

        city_name = weather_data.json()['name']
        weather = weather_data.json()['weather'][0]['description']
        temp = round(weather_data.json()['main']['temp'])

        print(f'Погода в городе {city_name}:\n'
              f'{weather.capitalize()}, температура {temp}°C\n')

    except:
        print("Некорректное название города. Попробуйте еще раз, пожалуйста\n")
