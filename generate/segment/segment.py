import random

class Segment:

	def __init__(self, length, distortionMax=0, distortionMin=0, distortionCoef = 1, step = 1, **kwargs):	
		self.kwargs = kwargs	
		self.length = length
		self.step = step		
		self.distortionMax = distortionMax
		self.distortionMin = distortionMin	
		self.distortionCoef = distortionCoef

	def generate(self, time, base):
		result = []
		x = 0
		i = 0
		while(x <= self.length):
			value = base + self.getValue(x) + random.uniform(self.distortionMin, self.distortionMax)
			result.append([time + i, value])
			i += 1
			x += self.step
		return [result, time + i]