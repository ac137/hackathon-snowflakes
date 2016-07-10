# test stuff 

import unittest
from numpy import array, concatenate, insert, vstack, append
from helper_functions import average_nearest 

u = array([[[1,2,3,4],[9,8,6,4],[21,23,25,26],[3,2,4,3]],
	[[2,5,3,1],[7,4,3,2],[4,30,2,19],[2,8,12,18]],
	[[5,46,30,84],[1,8,3,2],[0,3,2,1],[4,8,0,2]],
	[[9,6,1,5],[8,38,90,1],[3,3,3,3],[9,3,2,4]]],dtype=float)

mid_vals = array([[[2,5,3,1],[7,10.8,3.6,5.4],[4,13.8,9.8,13.4],[2,8,12,18]],
[[5,46,30,84],[1,12.4,26.6,18.4],[0,22,2.2,2.0],[4,8,0,2]]],dtype=float)

class TestAverage(unittest.TestCase):
	def test(self):
		self.assertEqual(u_av, average_nearest(u))

print u
print average_nearest(u)


if __name__ == '__main__':
	unittest.main()