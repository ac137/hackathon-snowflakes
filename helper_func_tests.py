# test stuff 

import unittest
from numpy import array, concatenate, insert, vstack, append, swapaxes, zeros
from helper_functions_marymod import average_nearest 

#u = array([[[1,2,3,4],[9,8,6,4],[21,23,25,26],[3,2,4,3]],
#	[[2,5,3,1],[7,4,3,2],[4,30,2,19],[2,8,12,18]],
#	[[5,46,30,84],[1,8,3,2],[0,3,2,1],[4,8,0,2]],
#	[[9,6,1,5],[8,38,90,1],[3,3,3,3],[9,3,2,4]]],dtype=float)

#u = swapaxes(u,0,2)
#u = swapaxes(u,0,1)

k = array([[[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]],
	[[2,1,4,3,3,4],[6,7,4,2,9,2],[80,53,24,13,28,35],[3,4,2,5,7,0],[7,24,63,29,30,20],[2,5,3,6,4,8]],
	[[3,78,25,5,3,2],[26,7,20,58,6,52],[24,65,2,0,9,5],[8,2,4,9,3,1],[2,4,3,5,6,3],[24,65,46,20,35,24]],
	[[24,53,38,40,24,6], [84,25,35,43,20,90],[25,41,29,51,20,25],[28,13,24,53,20,35],[46,35,26,36,74,35],[2,5,3,7,6,4]],
	[[48,20,58,4,20,24],[35,24,46,76,3,53],[92,35,64,93,21,24],[31,24,54,65,20,53],[2,54,3,76,5,2],[6,4,3,5,4,4]],
	[[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]], dtype=float)

k = swapaxes(k,0,2)
k = swapaxes(k,0,1)

#u_av = average_nearest(u)

#mid_vals = array([[[2,5,3,1],[7,10.8,3.6,5.4],[4,13.8,9.8,13.4],[2,8,12,18]],
#[[5,46,30,84],[1,12.4,26.6,18.4],[0,22,2.2,2.0],[4,8,0,2]]],dtype=float)
#mid_vals = swapaxes(mid_vals,0,2)
#mid_vals = swapaxes(mid_vals,0,1)
#print mid_vals

# print u[:,:,0]
# print u[0,:,0]
# print u[:,:,1]
# print u[:,:,2]
# print u[:,:,3]

# class TestAverage(unittest.TestCase):
# 	def test(self):
# 		self.assertEqual(u_av, average_nearest(u))


v = average_nearest(k)
print v
print v[:,:,0]
print v[:,:,1]
print v[:,:,2]
print v[:,:,3]



# if __name__ == '__main__':
# 	unittest.main()