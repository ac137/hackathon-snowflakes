# snowflake thing

from numpy import ones, vstack, hstack, dstack, newaxis, shape,array

def get_nearest_neightbours_plane(arr, idx):
	# this function is kind of obsolete
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
	# ROW, COLUMN, DEPTH
	# sum of row above, row below, 1 column to the left
	u = arr[:-2,1:,1:-1] + arr[2:,1:,1:-1] + arr[1:-1,:-1,1:-1]
	# select alternating columns, exclude leftmost col, outer rows, outer layers:

	v = arr[1:-1,1::2,1:-1]
	w = arr[1:-1,2::2,1:-1]

	# take alternating rows & add values from lower/upper layers

	v[::2,:,:] = arr[1:-1:2,1::2,2:]
	v[1::2,:,:] = arr[2:-1:2,1::2,:-2]

	w[::2,:,:] = arr[1:-1:2,2::2,-2:]
	w[1::2,:,:] = arr[2:-1:2,2::2,2:]

	# divide by 5 to get average
	u /= 5. #this syntax is glorious

	# now need to recombine with original array arr
	# probably best to use some sort of numpy stack thing
	# a bunch of numpy stack things
	# ughghhh

	# array sandwich - add top & bottom

	u = vstack(([arr[0,1:-1,1:]],u,[arr[-1,1:-1,1:]]))
	u = hstack((arr[:,0,newaxis,1:],u))
	u = hstack((u, arr[:,-1,newaxis,1:]))
	# add column to the left, have all layers and rows now
	u = dstack((arr[:,:,0,newaxis],u))
	# we are done, ugh

	return u






