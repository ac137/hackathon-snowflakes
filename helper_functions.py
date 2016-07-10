# snowflake thing

# need to add weights at some point.

from numpy import ones, vstack, hstack, dstack, newaxis, shape, array, zeros

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
	u = arr[:-2,1:-1,1:-1] + arr[2:,1:-1,1:-1] + arr[1:-1,:-2,1:-1]
	# select alternating columns, exclude leftmost col, outer rows, outer layers:
	# this is okay
	v = arr[1:-1,1::2,1:-1]
	w = arr[1:-1,2::2,1:-1]

	# take alternating rows & add values from lower/upper layers

	# odd columns
	# add lower layer
	v[::2,:,:] = arr[1:-1:2,1::2,2:]
	# add upper layer
	v[1::2,:,:] = arr[2:-1:2,1::2,:-2]

	# even columns
	# add upper layer
	w[::2,:,:] = arr[1:-1:2,2::2,:-2]
	# add lower layer
	w[1::2,:,:] = arr[2:-1:2,2::2,2:]

	# now v,w are matrices corresponding to odd & even columns

	# initialize array with same shape as array
	k = zeros(shape(arr))
	k[1:-1,1::2,1:-1] += v
	k[1:-1,2::2,1:-1] += w

	# k is now an array which has the values from columns above & below
	# that we would like to add


	# divide by 5 to get average
	u /= 5. #this syntax is glorious

	# now need to recombine with original array arr
	# probably best to use some sort of numpy stack thing
	# a bunch of numpy stack things
	# ughghhh

	# array sandwich - add top & bottom

	# add top row and bottom row:

	u = vstack((arr[newaxis,0,1:,1:-1],u))
	u = vstack((u, arr[newaxis,-1,1:,1:-1]))
	# add column to left, have all rows missing layers
	u = hstack((arr[:,0,newaxis,1:-1],u))
	# have all rows, columns, add layers to top & bottom
	u = dstack((arr[:,:,0,newaxis],u))
	u = dstack((u,arr[:,:,-1,newaxis]))

	return u






