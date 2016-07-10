def average_nearest(arr):
	# rows, columns, depth
	even_cols = arr[:,::2,:]
	odd_cols = arr[:,1::2,:]

	even_cols_even_rows = even_cols[::2,:,:]
	even_cols_odd_rows = even_cols[1::2,:,:]

	odd_cols_even_rows = odd_cols[::2,:,:]
	odd_cols_odd_rows = odd_cols[1::2,:,:]

	