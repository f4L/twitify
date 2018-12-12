import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=f5cfa10d79f2a9b64e735f242e70e6f9&q='
city = input("City Name :")

url = api_address + city

json_data = request.get(url).json()

print(json_data)
