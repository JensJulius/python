import random

# Use chosen method for creating list, finding the first digit and printing the results
def fullSequence(calcMethod, listLength):
  if calcMethod == 1:
    createRandIntList(listLength)
  elif calcMethod == 2:
    createDoubles(listLength)
  elif calcMethod == 3:
    createFibonacci(listLength)
  else:
    createSquaredList(listLength)

  findFirstDigit()
  calculateTotals()
  print("Total of each beginning digit and their % of total: ")
  printTotals()

# Methods for creating different lists
def createRandIntList(listLength): # List of random integers
  listLength = int(listLength)
  for i in range(listLength):
    r = random.randint(1, listLength)
    li.append(r)

def createDoubles(listLength): # List of constantly doubling numbers
  listLength = int(listLength)
  f1 = 1
  for i in range(listLength):
    li.append(f1)
    f1 = f1 * 2

def createFibonacci(listLength): # Fibonacci sequence
  listLength = int(listLength)
  a, b = 0, 1
  for i in range(listLength):
    a, b = b, a + b
    li.append(a)
  return a

def createSquaredList(listLength): # List of squared numbers (1, 2, 4, 16, 256... n)
  listLength = int(listLength)
  a = 1
  for i in range(listLength):
    li.append(a)
    a = a * a
    if a == 1:
      a = a + 1

# Go through list and remove all digits except for the first in every number in list li
def findFirstDigit():
  for i in li:
    while i >= 10:
      i = i / 10
    first_digit_list.append(i)

# Calculate totals of every starting digit
def calculateTotals():
  for i in first_digit_list:
    i = int(i)
    final_list[i - 1] = final_list[i - 1] + 1

# Print the total amount of every starting digit
def printTotals():
  int = 1
  total = 0

  for i in final_list:
    total = i + total

  for i in final_list:
      p = float(i * 100.0 / total)
      if i < 10:
        print(int, ": ", i, " ....", p, "%")
      if i >= 10:
        print(int, ": ", i, "....", p, "%")
      int += 1
  print("==========\n")

# Reset lists to get ready for creating and parsing a new list.
def resetLists():
  global li
  global first_digit_list
  global final_list
  global listLength

  li = [ ]
  first_digit_list = [ ]
  final_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Create the gui
def gui():
  while True:
    resetLists()
    #calcMethod = 0
    #listLength = 0
    i = input("1 : Random String of integers\n2 : List of doubling numbers\n3 : Fibonacci Sequence\n4 : List of squared numbers\n5 : Exit\n\n  : ")
    i = int(i)
    if i == 1: # 1 : Random String of integers
      calcMethod = i
      listLength = input("\nHow long do you want the list to be?\n\n  :")
      fullSequence(calcMethod, listLength)
    if i == 2: # 2 : List of doubling numbers
      calcMethod = i
      listLength = input("\nHow long do you want the list to be? [min: 1 - max: 1028]\n\n  :")
      fullSequence(calcMethod, listLength)
    if i == 3: # 3 : Fibonacci Sequence
      calcMethod = i
      listLength = input("\nHow long do you want the list to be? [min: 1 - max: 1481]\n\n  :")
      fullSequence(calcMethod, listLength)
    if i == 4: # 4 : List of squared numbers
      calcMethod = i
      listLength = input("\nHow long do you want the list to be? [min: 1 - max: 12]\n\n  :")
      fullSequence(calcMethod, listLength)
    if i == 5: # 5 : Exit
      quit()
    if i not in range(1, 6):
     print("\nInvalid option. Please try again... I believe in you\n")

def runScript():
  while True:
    gui()

if __name__ == '__main__':
  runScript()
