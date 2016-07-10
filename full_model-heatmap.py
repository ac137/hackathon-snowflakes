###################################################################################################################
##      Snowflake Simulation code
##      created by Alex Cabaj and Mary Miedema
##      (cite paper)
##
###################################################################################################################

from final_functions import *
from numpy import *
import pickle
import matplotlib.pyplot as plt

# set user-varied parameters
# alpha is an indication of temperature
alpha = 1
# beta is an indication of saturation, 0 < beta < 1
beta = .4

# choose scale of model grid;
    # side_len should be an even integer
side_len = 40
size_condition = False
# create border array
BORDER = zeros((side_len,side_len,side_len),dtype=bool)
BORDER[5,:,:] = BORDER[side_len-5,:,:] = BORDER[:,5,:] = BORDER[:,side_len-5,:] = BORDER[:,:,5] = BORDER[:,:,side_len-5] = True

# initialize state array with background saturation beta;
    # ice crystals valued at 1
    # place single ice crystal at centre of grid
S = beta*ones((side_len,side_len,side_len))
S[side_len/2,side_len/2,side_len/2] = 1.0

# initialize array containing indices of receptive cells
R = zeros((side_len,side_len,side_len),dtype=bool)
R[side_len/2,side_len/2,side_len/2] = True
# initialize array to be used for index addition
z = zeros((side_len,side_len),dtype=bool)
# initialize time & data
t_steps = []
state_data = []


##def model_step(alpha, beta,S,R):
##    # split state array in two;
##        # one with zeros in non-receptive cells
##        # we consider material in the remaining 
##        # receptive cells to be bound in place
##    S_R = S[R]
##        # one with zeros in receptive cells
##        # (and thus containing material free to diffuse)
##    S_NR = S[invert(R)]
##
##    # average material over non-receptive cells
##    S_NR_AVG = average_nearest(S_NR, beta)
##
##    # recombine into single state array
##    S_2 = S_R + S_NR_AVG
##
##    # find positions of ice cells and nearest neighbours
##    R, I = receptive_ind(S_2, z)
##    S = copy(S_2)
##    # state value cannot exceed 1
##    S[I] = 1.0
##    
##    # sum over borders of receptive array to
##        # check that snowflake has not outgrown model
##    if any(BORDER*I) == True:
##        size_condition = True
##        print "Snowflake has outgrown the grid! Ending simulation."
##
##    return S, R

# if this doesn't work, try creating g file for each time step
#g = open('snowflake_model'+str(beta)+'.p', 'w')   # create pickle file

        
# initialize time step tracker
j = 1
while size_condition == False:
    # get matrix with ones in positions of receptive cells
    POS = zeros((side_len,side_len,side_len))
    POS[R] = 1.
    # split state array in two;
        # one with zeros in non-receptive cells
        # we consider material in the remaining 
        # receptive cells to be bound in place
    S_R = copy(S)*POS
        # one with zeros in receptive cells
        # (and thus containing material free to diffuse)
    S_NR = copy(S)*invert(R)

    # average material over non-receptive cells
    S_NR_AVG = average_nearest(S_NR, beta,side_len)

    # recombine into single state array
    S_2 = S_R + S_NR_AVG

    # find positions of ice cells and nearest neighbours
    R, I = receptive_ind(S_2, z, side_len)
    S = copy(S_2)
    # state value cannot exceed 1
    S[I] = 1.0
    
    # sum over borders of receptive array to
        # check that snowflake has not outgrown model
    if any(BORDER*I) == True:
        size_condition = True
        print "Snowflake has outgrown the grid! Ending simulation."

    # advance time step
    j += 1
    if j%40 == 0:
        print "Time step: ", j

    print sum(I)

    t_steps.append(j)
    state_data.append(S)
    
# write data
# pickle.dump(array(state_data), g)
  
#g.close()

u = state_data[5]
v = u[:,:,10]

print shape(v)

im = plt.imshow(v, cmap='Blues')
plt.colorbar(im, orientation='horizontal')
plt.show()



