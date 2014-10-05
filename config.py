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
dataset = [	
	# first type of trajectories
	{					
		'name': 'normal',					
		#count of creating trajectories
		'count': 10,
		#definition of trajectories by segments
		'segments': [					
			CubeSegment(10, step=0.5, distortionMin=-5, distortionMax=5),
			MinusCubeSegment(10),
			ArcSegment(10),
			DownLineSegment(10),
			UpLineSegment(10),
			FullSquareSegment(10),
			HalfSquareSegment(10),
		]
	},
	#another type of trajectories
	{
		'name': 'bad',					
		'count': 10,
		'segments': [
			CubeSegment(10, step=0.5),
			MinusCubeSegment(10),
			ArcSegment(10),
			DownLineSegment(10),
			DownLineSegment(10),
			UpLineSegment(10),
			FullSquareSegment(10),
			HalfSquareSegment(10),
		]
	}
]