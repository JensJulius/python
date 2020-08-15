if __name__ == '__main__':
	n = int(input())
	arr = map(int, input().split())

	s_arr = sorted(arr, reverse=True)
	print(s_arr)

	for i in s_arr:
		if i == s_arr[0]:
			continue
		else:
			print(i)
			break
	# for i in arr:
	# 	if i > largest_digit:
	# 		second_largest_digit = largest_digit
	# 		largest_digit = i

	# 	elif i > second_largest_digit and i < largest_digit:
	# 		smallest_digit = second_largest_digit
	# 		second_largest_digit = i

	# 	else:
	# 		smallest_digit = i

	# print(second_largest_digit)
