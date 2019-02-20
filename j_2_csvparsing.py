# import libraries
import csv
import json


# open json file to read the content..
with open('data.json') as mfile:
	data = mfile.read()

# it will save the json content in the form of python dictionary(key,value)..
obj = json.loads(data)


#sample dictionary 
...
dict = {"name" : "niket",
		"age"  : 21,
		"place" : "mysore"
}
...

# it will opne a new csv file in write mode
with open('output.csv','w') as output:
	writer = csv.writer(output)
	
	# to loop through the dictionary..
	for key,value in obj.items():
		writer.writerow([key,value])