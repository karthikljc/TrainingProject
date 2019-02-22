import json 
import csv

with open('data.json') as f:
		data = f.read()
	
obj = json.loads(data)


for keys,values in obj.items(): 
	print(keys, ':', values)
	
	


	