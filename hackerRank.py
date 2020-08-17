#!/bin/python3

if __name__ == '__main__':
	phoneBook = {}
	n = int(input())
	phoneBook = map(int, input().rstrip().split())
	print(phoneBook)
	# for i in range(n):
	# 	name = input().rstrip().split()
	# 	number = input().rstrip().split()
	# 	print(name)
	# 	print(number)

	while True:
		name = input().lower()
		if name not in phoneBook:
			print("Not found")
		else:
			phoneNumber = phoneBook.get(name)
			print(name + "=" + phoneNumber)
