import json
from random import randint

idlist = {}
with open('metadata.json') as json_data:
	idlist = json.load(json_data)

total = 0
for key,item in idlist.items():
	total += item['count']

def generate_incident():
	num = randint(0, total)
	temp = 0
	id = ''
	desc = ''
	out = False
	for key,item in idlist.items():
		for x in range (temp, temp + item['count']):
			temp += 1
			if (temp >= num):
				out = True
				id = key
				desc = item['description']
				break
				
		if out:
			break
	return [id, desc]

print(generate_incident())