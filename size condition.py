from numpy import *

size_condition = False
side_len = 20

I = zeros((side_len,side_len,side_len),dtype=bool)
I[side_len-5,side_len/2,side_len/2] = True

# create border array
BORDER = zeros((side_len,side_len,side_len),dtype=bool)
BORDER[5,:,:] = BORDER[side_len-5,:,:] = BORDER[:,5,:] = BORDER[:,side_len-5,:] = BORDER[:,:,5] = BORDER[:,:,side_len-5] = True

# test if ice crystals have crossed boundary
if any(BORDER*I) == True:
    size_condition = True
    print "Snowflake has outgrown the grid! Ending simulation."
