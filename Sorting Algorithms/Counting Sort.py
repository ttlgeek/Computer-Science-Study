def counting_sort(num_list):
	list_size = len(num_list)
	num_count = [0] * list_size
	for num in num_list:
		num_count[num] += 1
	sorted_list = []
	for i in range(list_size):
		nums = [i] * num_count[i]
		sorted_list += nums
	return sorted_list

print(counting_sort([2, 3, 8, 7, 1, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2]))