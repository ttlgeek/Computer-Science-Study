def selection_sort(num_list):
	arr_size = len(num_list)
	for i in range(arr_size  - 1):
		current_minimum_index = i
		current_minimum = num_list[current_minimum_index]
		for k in range(current_minimum_index, arr_size):
			if num_list[k] < current_minimum:
				current_minimum_index = k
				current_minimum = num_list[current_minimum_index]
		num_list[current_minimum_index], num_list[i] = num_list[i], num_list[current_minimum_index]

	return num_list

print(selection_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))