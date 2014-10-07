from generate.segment.arc import ArcSegment
from generate.segment.cube import CubeSegment
from generate.segment.minuscube import MinusCubeSegment
from generate.segment.downline import DownLineSegment
from generate.segment.upline import UpLineSegment
from generate.segment.fullsquare import FullSquareSegment
from generate.segment.halfsquare import HalfSquareSegment

#result path
path = './generated_data'

#definition of creating dataset
dataset = {
	'aliases': {
		'A': CubeSegment(10),
		'B': MinusCubeSegment(10),
		'C': ArcSegment(10),
		'D': DownLineSegment(10),
		'E': UpLineSegment(10),
		'F': FullSquareSegment(10),
		'G': HalfSquareSegment(10),
		'H': CubeSegment(10)
	},	

	'classes': {
		# first type of trajectories
		'normal': {							
			#count of creating trajectories
			'count': 10,
			#count of segments
			'length': 10,		
		},

		#another type of trajectories
		'bad1': {										
			#count of creating trajectories
			'count': 10,
			#count of segments
			'length': 10, 
			'abnormalSequence': 'ABCD'
		},

		#another type of trajectories
		'bad2_': {										
			#count of creating trajectories
			'count': 10,
			#count of segments
			'length': 10, 
			'abnormalSequence': 'BBB'
		}
	}	
}