import csv
import json
import numpy as np
from tqdm import tqdm
#from difflib import SequenceMatcher

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

file = open('Tables/FFD info 2016.csv', 'r')
file2 = open('Tables/Incident ID List.csv', 'r')
data = csv.reader(file)
data2 = csv.reader(file2)

incidents = []
next(data)
for row in data:
	item = row[5]
	if (item == ''): 
		continue
	incidents.append(item)
	
idlist = {}
for row in data2:
	idlist[row[0]] = {'description':row[1], 'count':0}
	
print(len(incidents))
for incident in tqdm(incidents):
	bestID = 0
	bestRatio = 5000000
	for key,item in idlist.items():
		match = levenshtein(item['description'], incident)
		if (match < bestRatio):
			bestID = key
			bestRatio = match
			
	idlist[str(bestID)]['count'] += 1

with open('metadata.json', 'w') as f:
	json.dump(idlist,f)