# snowflake thing

from numpy import ones

def get_nearest_neightbours_plane(arr, idx):
	# index tuple of row, column
	r,c = idx[0],idx[1]
	n1, n2, n3 = None, None, None
	try:
		n1 = arr[r + 1,c]
	except IndexError:
		pass
	try:
		n2 = arr[r - 1, c]
	except IndexError:
		pass
	try:
		n3 = arr[r,c - 1]
	except IndexError:
		pass
	return n1, n2, n3

#b is a parameter

def initialize_array(side_len, b):
	# initialize 3d array, for a background value b
	arr = ones((side_len,side_len,side_len))*b
	mid = side_len/2
	arr[mid,mid,mid] = 1.0
	return arr

def average_nearest(arr):
	# welcome to slicing hell
	# sum of 1 column to the left, row above, and row below
	u = arr[0:-2,1:,1:-1] + arr[2:,1:,1:-1] + arr[1:-1,:-1,1:-1]
	# average alternating columns with layer above:
	v = arr[1:-1,1::2,1:-1] # odd columns
	w = arr[1:-1,2::2,1:-1] # even columns
	# add layer above to alternating rows
	v[::2,:,:] += arr[1:-1:2,1::2,2:]
	# add layer below to alternating rows
	v[1::2,:,:] += arr[2:-1:2,1::2,0:-2]
	# add layer below
	w += arr[1:-1,2::2,:-2]
	u[:,::2,1:-1] += v
	u[:,1::2,1:-1] += w
