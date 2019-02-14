import json

# read file
with open('currentweather.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

# show values
print("coord: " + str(obj['coord']))
print("weather: " + str(obj['weather']))
print("base: " + str(obj['base']))
print("main: " + str(obj['main']))
print("visibility: " + str(obj['visibility']))
print("wind: " + str(obj['wind']))
print("clouds: " + str(obj['clouds']))
print("dt: " + str(obj['dt']))
print("sys: " + str(obj['sys']))
print("id: " + str(obj['id']))
print("name: " + str(obj['name']))
print("cod: " + str(obj['cod']))