import csv
from datetime import datetime

data = csv.reader(open('FFD info 2016.csv', 'r'))
next(data)
	
sumTime = 0
sumItems = 0
elements = []

column1 = 0
column2 = 4
	
for row in data:
	callItem = 0
	if (row[column1] == ''):
		continue
	callItem = row[column1]
	callInfo = datetime.strptime(callItem, '%m/%d/%Y %H:%M:%S')
	
	departItem = 0
	if (row[column2] == ''):
		continue
	departItem = row[column2]
	departInfo = datetime.strptime(departItem, '%m/%d/%Y %H:%M:%S')
	
	sumItems += 1
	timeTaken = (departInfo - callInfo).total_seconds()
	elements.append(timeTaken)
	sumTime += timeTaken
	
print("Average time: " + str(sumTime / sumItems))
print("Median time: " + str(elements[(int)(len(elements)/2)]))