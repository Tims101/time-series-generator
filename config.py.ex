from generate.segment.arc import ArcSegment
from generate.segment.cube import CubeSegment
from generate.segment.minuscube import MinusCubeSegment
from generate.segment.downline import DownLineSegment
from generate.segment.upline import UpLineSegment
from generate.segment.fullsquare import FullSquareSegment
from generate.segment.halfsquare import HalfSquareSegment

#result path
path = './generated_data'
csv_header = ['time', 'row_1']

#definition of creating dataset
dataset = {
	'gauss': {
		'mu': 0,
		'sigma': 2
	},

	'length_deformation': {
		'max': 2,
		'min': 1
	},

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
			'count': 2,
			#count of segments
			'length': 10,		
			'removeSequences': ['ABCD', 'CCDDHH']
		},

		#another type of trajectories
		'bad1': {										
			#count of creating trajectories
			'count': 2,
			#count of segments
			'length': 10, 
			'abnormalSequence': 'ABCD',
			'removeSequences': ['CCDDHH']
		},

		#another type of trajectories
		'bad2': {										
			#count of creating trajectories
			'count': 2,
			#count of segments
			'length': 10, 
			'abnormalSequence': 'CCDDHH',
			'removeSequences': ['ABCD']
		}
	}	
}