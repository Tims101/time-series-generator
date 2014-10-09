import os
import csv
import random

from generate.trajectory import Trajectory

import config

if not os.path.exists(config.path):
	os.makedirs(config.path)	

aliases = config.dataset['aliases']
alphabet = list(aliases.keys())

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

def generateSegmentsFromString(string):
	result = []
	for char in string:
		result.append(aliases[char])
	return result		

def getRandomSubstring(length):
	result = ''
	for i in range(length):
		result += random.choice(alphabet)
	return result


def getOccurencesCount(str, substrings):
	count = 0
	for substr in substrings:
		count += len(list(find_all(str, substr)))
	return count

#very bad code
def generateSegments(data):
	length = data['length']	
	result = getRandomSubstring(length)
	do_again = False

	while (True):

		if 'abnormalSequence' in data:
			abnormal = data['abnormalSequence']		
			abnormal_length = len(abnormal)		
			occurences = list(find_all(result, abnormal))
			
			while (len(occurences) > 0):
				result = getRandomSubstring(length)
				occurences = list(find_all(result, abnormal))

			if len(occurences) == 0: 
				pos = random.randint(0, length - abnormal_length)
				result = result[:pos] + data['abnormalSequence'] + result[pos + abnormal_length:]

				occurences = list(find_all(result, abnormal))
				
				if (len(occurences) != 1):
					continue
					
		do_again = False

		if 'removeSequences' in data:
			while (getOccurencesCount(result, data['removeSequences']) != 0):
				result = getRandomSubstring(length)

				if 'abnormalSequence' in data:
					do_again = True
					break

		if do_again:
			continue
		
		if 'abnormalSequence' in data:
			print(result.replace(abnormal, '_{0}_'.format(abnormal)))	
		else:
			print(result)
		
		break

	return generateSegmentsFromString(result)

def handleClass(name, data):
	dir = os.path.join(config.path, name).replace("\\","/")
	if not os.path.exists(dir):
		os.makedirs(dir)

	print('Generate segments...')
	if 'abnormalSequence' in data:	
		print('Abnormal: {0}'.format(data['abnormalSequence']))
	for i in range(data['count']):			
		segments = generateSegments(data)

		trajectory = Trajectory(segments)	
		result = trajectory.generate()

		file = os.path.join(config.path, name, '{0}_{1}.csv'.format(name, i)).replace("\\","/")		
		with open(file, "w") as f:
		    writer = csv.writer(f, delimiter=';', lineterminator='\n')
		    writer.writerows(result)

for name, data in config.dataset['classes'].items():
	print('Handle class: {0}'.format(name))
	handleClass(name, data)
	print('')

print('Finished')
	






