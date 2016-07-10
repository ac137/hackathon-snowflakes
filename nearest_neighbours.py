## finds array with indices of nearest neighbours and ice cells (ie. receptive cells) ##

from numpy import *

#R = random.rand(10,10,10)

#z = zeros(l,dtype=bool)

def checkerboard(side_len, boolean):
    '''Creates a "cubic checkerboard" of sorts.
        side_len: choose an even-valued integer for side length
        boolean: set to True if wanting True/False states
                 set to False if wanting 1/0 states
    '''
    halflen = side_len/2
    if boolean == True:
        even_row = r_[halflen*[False,True]]
        odd_row = r_[halflen*[True,False]]
        even_plane = vstack(halflen*(even_row,odd_row))
        odd_plane = vstack(halflen*(odd_row,even_row))
        cube = dstack(halflen*(even_plane,odd_plane))
        return cube
    elif boolean == False:
        even_row = r_[halflen*[0,1]]
        odd_row = r_[halflen*[1,0]]
        even_plane = vstack(halflen*(even_row,odd_row))
        odd_plane = vstack(halflen*(odd_row,even_row))
        cube = dstack(halflen*(even_plane,odd_plane))
        return cube
    else:
        return "Argument not recognized."


##def receptive(arr,z):
##    ''' Function to find indices of all receptive cells              
##        arr: recombined matrix
##        z: define outside loop as z = zeros(side_len, side_len,dtype=bool)
##
##        Note that invert() function can be used to find indices of non-receptive cells.
##    '''
##    # could always restrict to ignore boundaries
##
##    # get indices of ice cells
##    i_I = arr >= 1.0
##
##    # get indices of neighbouring cells in same plane
##    i_L = hstack((z.reshape(side_len,1,side_len), i_I[:,:-1,:]))
##    i_T = vstack((z.reshape(1,side_len,side_len), i_I[:-1,:,:]))
##    i_B = vstack((i_I[1:,:,:],z.reshape(1,side_len,side_len))
##
##    # check for 2d case whether to swap z, I_i in one case
##
##    # get indices of neighbouring cells in adjacent planes
##    # odd columns, rows above
##    OA = i_I[::2,::2,:]
##    i1 = dstack((z.reshape(side_len,side_len,1),OA[]))
##    # odd columns, rows below
##    i2 = dstack((OB[],z.reshape(side_len,side_len,1)))
##    # all even columns
##    i_V = i1 + i2
##    # even columns, rows above
##    i3 = dstack((z.reshape(side_len,side_len,1),EA[]))
##    # even columns, rows below
##    i4 = dstack((EB[],z.reshape(side_len,side_len,1)))
##    # all even columns
##    iW = i3 + i4
##
##    # return indices of all receptive cells
##    IND = i_I + i_L + i_T + i_B
##    return IND
