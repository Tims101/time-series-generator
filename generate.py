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
        start += len(sub) # use start += 1 to find overlapping matches

def generateSegmentsFromString(string):
	result = []
	for char in string:
		result.append(aliases[char])
	return result		

def generateSegments(data):
	length = data['length']	
	result = ''

	for i in range(length):
		result += random.choice(alphabet)

	if 'abnormalSequence' in data:
		abnormal = data['abnormalSequence']		
		abnormal_length = len(abnormal)		
		occurences = list(find_all(result, data['abnormalSequence']))
		if len(occurences) >= 2:
			for i in range(1, len(occurences)):
				#TODO: remove bad things
				result[i, i + abnormal_length] = ''.join(random.sample(abnormal, abnormal_length))
		elif len(occurences) == 0: 
			pos = random.randint(0, length - abnormal_length)
			result = result[:pos] + data['abnormalSequence'] + result[pos + abnormal_length:]			
		print(result.replace(abnormal, '_{0}_'.format(abnormal)))
	else:
		print(result)	
	
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
	






