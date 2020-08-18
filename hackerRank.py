#!/bin/python3

if __name__ == '__main__':
	phoneBook = {}
	n = int(input())

	for i in range(n):
		nameAndNumber = input().rstrip().split()
		name, number = nameAndNumber
		phoneBook[name] = number

	print(phoneBook)

	while True:
		name = input().lower()

		if name not in phoneBook:
			print("Not found")
		else:
			phoneNumber = phoneBook.get(name)
			print(name + "=" + phoneNumber)
