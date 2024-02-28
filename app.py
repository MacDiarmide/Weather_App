import requests

api_key = 'ad6e3d1262d3f8dc675a19aaa2ee7702'

user_input = input('Введите название города: ')

# a Response object:
weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}')

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

print(f'Погода в {user_input}: {weather}\n'
      f'Температура в {user_input} {temp} градусов Цельсия')