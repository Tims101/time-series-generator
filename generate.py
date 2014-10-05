import os
import csv

from generate.trajectory import Trajectory

import config

def handleDatasetItem(item):
	dir = os.path.join(config.path, item['name']).replace("\\","/")
	if not os.path.exists(dir):
		os.makedirs(dir)	
	trajectory = Trajectory(item['segments'])

	for i in range(1, item['count'] + 1):
		result = trajectory.generate()

		file = os.path.join(config.path, item['name'], '{0}{1}.csv'.format(item['name'], i)).replace("\\","/")
		with open(file, "w") as f:
		    writer = csv.writer(f, delimiter=';', lineterminator='\n')
		    writer.writerows(result)


if not os.path.exists(config.path):
	os.makedirs(config.path)	

for item in config.dataset:
	handleDatasetItem(item)