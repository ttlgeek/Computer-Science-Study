def bubble_sort(num_list):
	swaps = 1
	while swaps > 0:
		swaps = 0
		for i in range(len(num_list) - 1):
			if num_list[i] > num_list[i + 1]:
				swaps += 1
				num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]

	return num_list