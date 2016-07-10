# snowflake thing

# need to add weights at some point.

from numpy import ones, vstack, hstack, dstack, newaxis, shape,array

side_len = 6

def checkerboard(side_len, boolean, num):
    '''Creates a "cubic checkerboard" of sorts.
        side_len: choose an even-valued integer for side length
        boolean: set to True if wanting True/False states
                 set to False if wanting 1/0 states
        num: allows for choice of checkerboard startpoint
             set to 0 if wanting False/0 value at (0,0,0)
             set to 1 if wanting True/1 value at (0,0,0)
    '''
    halflen = side_len/2
    if boolean == True:
        even_row = r_[halflen*[False,True]]
        odd_row = r_[halflen*[True,False]]
        even_plane = vstack(halflen*(even_row,odd_row))
        odd_plane = vstack(halflen*(odd_row,even_row))
        if num == 0:
            cube = dstack(halflen*(even_plane,odd_plane))
        elif num == 1:
            cube = dstack(halflen*(odd_plane,even_plane))
        else:
            print "Argument for checkerboard startpoint (num) not recognized."
        return cube
    elif boolean == False:
        even_row = r_[halflen*[0,1]]
        odd_row = r_[halflen*[1,0]]
        even_plane = vstack(halflen*(even_row,odd_row))
        odd_plane = vstack(halflen*(odd_row,even_row))
        if num == 0:
            cube = dstack(halflen*(even_plane,odd_plane))
        elif num == 1:
            cube = dstack(halflen*(odd_plane,even_plane))
        else:
            print "Argument for checkerboard startpoint (num) not recognized."
        return cube
    else:
        print "Argument for Boolean variable not recognized."

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

	# sum of adjacent planes
	c1 = checkerboard(side_len, False, 0)
	c2 = checkerboard(side_len, False, 1)
	v = c1*arr[1:-1,1:-1,2:] + c2*arr[1:-1,1:-1,:-2]
	w = arr[1:-1,1:-1,1:-1]

	k = u + v + w
	
	# k is now an array which has the values from columns above & below
	# that we would like to add


	# divide by 5 to get average
	k /= 5. #this syntax is glorious

	# now need to recombine with original array arr
	# probably best to use some sort of numpy stack thing
	# a bunch of numpy stack things
	# ughghhh

	# array sandwich - add top & bottom

	# add top row and bottom row:

	k = vstack((arr[newaxis,0,1:,1:-1],k))
	k = vstack((k, arr[newaxis,-1,1:,1:-1]))
	# add column to left, have all rows missing layers
	k = hstack((arr[:,0,newaxis,1:-1],k))
    k = hstack((k,arr[:,-1,newaxis,1:-1]))
	# have all rows, columns, add layers to top & bottom
	k = dstack((arr[:,:,0,newaxis],k))
	k = dstack((u,arr[:,:,-1,newaxis]))

	return k
