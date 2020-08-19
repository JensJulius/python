#!/bin/python3

if __name__ == '__main__':
	n = int(input())

	binList = []
	result = 1
	prev = 0
	consec = 1

	while n > 0:
		if (n % 2) == 0:
			binList.append(0)
			n = int(n / 2)
		elif (n % 2) != 0:
			binList.append(1)
			n = int(n / 2)
	binList.reverse()
	print(binList)

	for i in binList:
		if i == 1 and i == prev:
			result += 1
			if result > consec:
				consec = result
		elif i == 0:
			result = 1
		prev = i
	print(consec)
