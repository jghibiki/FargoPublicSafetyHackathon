import csv
import json
import numpy as np
from tqdm import tqdm
from datetime import datetime

def levenshtein(source, target):
    if len(source) < len(target):
        return levenshtein(target, source)

    # So now we have len(source) >= len(target).
    if len(target) == 0:
        return len(source)

    # We call tuple() to horse strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = np.array(tuple(source))
    target = np.array(tuple(target))

    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1

        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]
	
def get_time(item1, item2):
	if (item1 == '' or item2 == ''):
		return 0
	info1 = datetime.strptime(item1, '%m/%d/%Y %H:%M:%S')
	info2 = datetime.strptime(item2, '%m/%d/%Y %H:%M:%S')
	return (info1 - info2).total_seconds()

file = open('Tables/FFD info 2016.csv', 'r')
file2 = open('Tables/Incident ID List.csv', 'r')
data = csv.reader(file)
data2 = csv.reader(file2)

incidents = []
next(data)
for row in data:
	item = row
	if (item == ''): 
		continue
	incidents.append(item)
	
idlist = {}
for row in data2:
	idlist[row[0]] = {'description':row[1], 'count':0, 'callTime':0, 'leaveTime':0, 'travelTime':0, 'eventTime':0}
	
print(len(incidents))
for incident in tqdm(incidents):
	bestID = 0
	bestRatio = 5000000
	for key,item in idlist.items():
		match = levenshtein(item['description'], incident[5])
		if (match < bestRatio):
			bestID = key
			bestRatio = match
			
	idlist[str(bestID)]['callTime'] += get_time(incident[1], incident[0])
	idlist[str(bestID)]['leaveTime'] += get_time(incident[2], incident[1])
	idlist[str(bestID)]['travelTime'] += get_time(incident[3], incident[2])
	idlist[str(bestID)]['eventTime'] += get_time(incident[4], incident[3])
	idlist[str(bestID)]['count'] += 1
	
for key,item in idlist.items():
	if (item['count'] > 0):
		item['callTime'] = item['callTime'] / item['count']
		item['leaveTime'] = item['leaveTime'] / item['count']
		item['travelTime'] = item['travelTime'] / item['count']
		item['eventTime'] = item['eventTime'] / item['count']

with open('metadata.json', 'w') as f:
	json.dump(idlist,f)