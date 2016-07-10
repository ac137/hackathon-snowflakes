# snowflake thing

from numpy import ones, concatenate

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
	# INDEXING IS LAYER, ROW, COLUMN!!!

	# sum of 1 column to the left, row above, and row below
	u = arr[1:-1,:-2,1:] + arr[1:-1,2:,1:] + arr[1:-1,1:-1,:-1]
	# average alternating columns with layer above:
	v = arr[1:-1,1:-1,1::2] # odd columns
	w = arr[1:-1,1:-1,2::2] # even columns
	# add layer above to alternating rows
	v[:,::2,:] += arr[2:,1:-1:2,1::2]
	# add layer below to the other rows
	v[:,1::2,:] += arr[0:-2,2:-1:2,1::2]
	# add layer below to the alternating rows
	w[:,::2,:] += arr[:-2,1:-1:2,2::2]
	# add layer above to the other rows
	w[:,1::2,:] += arr[2:,2:-1:2,2::2]
	# combine this whole ungodly mess
	u[1:-1,:,::2] += v
	u[1:-1,:,1::2] += w
	# divide by 5 to get average
	u /= 5. #this syntax is glorious

	# now need to recombine with original array arr
	# probably best to use some sort of numpy stack thing
	# a bunch of numpy stack things
	# ughghhh

	# array sandwich - add top & bottom
	u = concatenate(arr[0,1:-1,1:],u,arr[-1,1:-1,1:], axis=0)
	# add row above and below, we have all the layers now
	u = concatenate(arr[:,0,1:],u,arr[:,-1,1:], axis=1)
	# add column to the left, have all layers and rows now
	u = concatenate(arr[:,:,0],u,axis=2)

	# we are done, ugh
	return u






