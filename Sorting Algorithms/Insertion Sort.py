def insertion_sort(num_list):
	list_size = len(num_list)
	for i in range(1, list_size):
		curr_number = num_list[i]
		j = i - 1
		while num_list[j - 1] > curr_number and j > 0:
			num_list[j] = num_list[j - 1]
			j -= 1
		num_list[j] = curr_number
	return num_list