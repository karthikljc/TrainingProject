import json

with open('data.json') as mfile:
	data = mfile.read()

obj = json.loads(data)

print(obj)








