from numpy import *

side_len = 4

#arr = random.rand(side_len,side_len,side_len)
arr = zeros((side_len,side_len,side_len))
arr[0,2,1]=.98
z = zeros((side_len,side_len),dtype=bool)

def checkerboard(side_len, boolean, num):
    '''Creates a "cubic checkerboard" of sorts.
        side_len: choose an even-valued integer for side length
        boolean: set to True if wanting True/False states
                 set to False if wanting 1/0 states
        num: allows for choice of checkerboard startpoint
             set to 0 if wanting False/0 value at (0,0,0)
             set to 1 if wanting Turue/1 value at (0,0,0)
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


def receptive_ind(arr, z):
    ''' Function to find indices of all receptive cells              
        arr: recombined matrix
        z: define outside loop as z = zeros(side_len, side_len,dtype=bool)
    '''

    # get indices of ice cells
    i_I = arr >= 1.0
    
    # get indices of neighbouring cells in same plane
        # from left column
    i_LEFT = hstack((z.reshape(side_len,1,side_len), i_I[:,:-1,:]))
        # from adjacent rows
    i_TOP = vstack((z.reshape(1,side_len,side_len), i_I[:-1,:,:]))
    i_BOTTOM = vstack((i_I[1:,:,:],z.reshape(1,side_len,side_len)))

    # get indices of neighbouring cells in adjacent planes
        # (adding indices down from neighbouring cells in the plane above)
    iA = checkerboard(side_len, True, 0)*i_I
    i_ABOVE = dstack((z.reshape(side_len,side_len,1),iA[:,:,:-1]))
        # (adding indices up from neighbouring cells in the plane below)
    iB = checkerboard(side_len, True, 1)*i_I
    i_BELOW = dstack((iB[:,:,1:],z.reshape(side_len,side_len,1)))
    
    # return indices of all receptive cells
    IND = i_I + i_LEFT + i_TOP + i_BOTTOM + i_ABOVE + i_BELOW
    # (also return indices of ice cells)
    return IND, i_I

print receptive_ind(arr,z)

def receptive_arr(arr, z):
    '''Returns array with ones indicating positions of receptive cells,
        zeros indicating positions of non-receptive cells.'''
    ind = receptive_ind(arr, z)
    new = arr
    new[ind] = 1
    new[invert(ind)] = 0
    return new
