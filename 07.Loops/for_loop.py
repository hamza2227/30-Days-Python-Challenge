# A for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).

# Example
# Print each fruit in a fruit list:
fruits = ["apple", "Banana", "Mangoe"]
for x in fruits:
    print(x)


# - Looping Through a String
for x in "Banana":
    print(x)


# - The break Statement
fruits = ["apple", "Banana", "Mangoe", "Cherry", "Grapes"]
for x in fruits:
    print(x)
    if x == "Mangoe":
        break

# ---
# Exit the loop when x is "banana", but this time the break comes before the print:
objects = ["table", "chair", "plate", "glass", "cup"]
for x in objects:
    if x == "plate":
        break
    print(x)
    

# - The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
# ---
objects = ["table", "chair", "plate", "glass", "cup"]
for x in objects:
    
    if x == "plate":
        continue
    print(x)


# - The range() Function:
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments
# by 1 (by default), and ends at a specified number.

for x in range(6):
  print(x)
  
  
# --- For Loops are used for sequential traversal. For example traversing a list, string or arrays etc. 
n = 4
for i in range(0, n):
    print(i)
# Explanation: This code prints the numbers from 0 to 3 (inclusive) using a for loop that iterates over a 
# range from 0 to n-1 (where n = 4).


# --- Example with List, Tuple, String, and Dictionary Iteration :
li = ["geeks", "for", "geeks"]
for i in li:
    print(i)

tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)
    
st = "geeks"
for i in st:
    print(i)

dt = dict({'x':123, 'y':456})
for i in dt:
    print("%s  %d" % (i, dt[i]))

set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)
    

# --- Iterating by the Index of Sequences
list = ["geeks", "for", "geeks"]
for index in range(list):
    print(list[index])
    

# --- Python Nested Loop
list1 = ["Apple", "Banana", "Orange"]
list2 = ["Red", "Yellow", "Orange"]
for fruits in list1:
    for color in list2:
        print(fruits + color)