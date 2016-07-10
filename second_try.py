from numpy import zeros, copy, shape

def average_nearest(arr):
	# rows, columns, depth

	sh = shape(arr)

	q_arr = copy(arr)

	even_cols = q_arr[:,::2,:]
	odd_cols = q_arr[:,1::2,:]

	# changing these slices changes the arrays even_cols, odd_cols
	even_cols_even_rows = even_cols[::2,:,:]
	even_cols_odd_rows = even_cols[1::2,:,:]

	odd_cols_even_rows = odd_cols[::2,:,:]
	odd_cols_odd_rows = odd_cols[1::2,:,:]

	even_cols_even_rows[:,:,:-1] = even_cols_even_rows[:,:,1:]
	even_cols_odd_rows[:,:,1:] = even_cols_odd_rows[:,:,:-1]

	odd_cols_even_rows[:,:,1:] = odd_cols_even_rows[:,:,:-1]
	odd_cols_odd_rows[:,:,:-1] = odd_cols_odd_rows[:,:,1:]


	# so now, q_arr stores the values of q we want.
	#q_arr is an nxnxn array

	# now, we just need to get the values of the adjacent indices

	p_sum = arr[2:,1:-1,:] + arr[:-2,1:-1,:] + arr[1:-1,:-2,:]
	# this is an (n-2)x(n-2)xn array

	tot_sum = copy(q_arr) # contains q-values
	tot_sum[1:-1,1:-1,:] += p_sum # now also added the 3 p-values
	tot_sum += arr # added the original value at the element
	tot_sum /= 5. # average it up
	return tot_sum








	