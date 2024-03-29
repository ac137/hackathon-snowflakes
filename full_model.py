##########################################################################################################################
##      Snowflake Growth Simulation                                                                                     ##
##      created by Alex Cabaj and Mary Miedema                                                                          ##
##      at the McGill Physics Hackathon                                                                                 ##
##      July 9th-10th, 2016                                                                                             ##
##                                                                                                                      ##
##      Our approach to snowflake crystallization was influenced by methods outlined by Ning and Reiter                 ##
##      (Computers & Graphics, 2007); all code used in this file and in "snowflake_functions.py" is our                 ##
##      own original implementation.                                                                                    ##
##                                                                                                                      ##
##########################################################################################################################

# import our analysis functions from "snowflake_functions.py"
from snowflake_functions import *
from numpy import *
import pickle

# set user-varied parameters
# alpha is an indication of temperature
alpha = 2
# beta is an indication of saturation, 0 < beta < 1
beta = .35

# choose scale of model grid;
    # side_len should be an even integer
side_len = 80
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
R[side_len/2-1:side_len/2+2,side_len/2-1:side_len/2+2,side_len/2-1:side_len/2+2] = True
# initialize array to be used for index addition
z = zeros((side_len,side_len),dtype=bool)
# initialize time & data
t_steps = []
state_data = []

# prepare to write to data
g = open('snowflake_model-'+str(alpha)+'-'+str(beta)+'.p', 'w')   # create pickle file
        
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
    POS = zeros((side_len,side_len,side_len))
    POS[invert(R)] = 1.
    S_NR = copy(S)*POS

    # average material over non-receptive cells
    S_NR_AVG = average_nearest(S_NR, alpha, beta, side_len)

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
    t_steps.append(j)
    
    state_data.append(S)
    # write data
    pickle.dump(array(state_data), g)

# plot data
import matplotlib.pyplot as plt
# take slice
slz = S[:,:,30]
vz = hstack(((fliplr(slz[:,40:]),slz[:,40:])))
slx = S[30,:,:]
vx = hstack(((fliplr(slx[:,40:]),slx[:,40:])))
im_z = plt.imshow(vz, cmap='Blues_r')
plt.colorbar(im_z, orientation='horizontal')
plt.show()
im_x = plt.imshow(vx, cmap='Blues_r')
plt.colorbar(im_x, orientation='horizontal')
plt.show()

g.close()
