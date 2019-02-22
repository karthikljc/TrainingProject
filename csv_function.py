#json to csv parsing using functions 


import csv
import json

def parser():
	with open('data.json') as mfile:
		data = mfile.read()
	
	obj = json.loads(data)


	with open('output.csv','w') as output:
		writer = csv.writer(output)
		for key,value in obj.items():
			writer.writerow([key,value])	
		
parser()