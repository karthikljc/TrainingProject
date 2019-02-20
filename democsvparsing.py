import csv


dict = {"name" : "niket",
"age"  : 21,
"place" : "mysore"
}

with open('output.csv','w') as output:
	writer = csv.writer(output)
	for key,value in dict.items():
		writer.writerow([key,value])
