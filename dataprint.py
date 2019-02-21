import json
import csv

inputfile = open('data.json')
outputfile = open('sample.csv', 'w')
data = json.loads(inputfile)
inputfile.close()

output = csv.writer(outputfile)

output.writerow(data[0].keys()) 

for (k,v) in data.items(): 
	print("Keys: " + k)
	print("value: " + str(v))
