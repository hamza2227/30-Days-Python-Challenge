## Boolean
# A boolean data type represents one of the two values: True or False.

print(True)
print(False)

## Operators
# Python language supports several types of operators. In this section, we will focus on few of them.

# Assignment Operators:
# Assignment operators are used to assign values to variables. Let us take = as an example.


# Arithmetic Operators:
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b

# Integers
print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2

# Floats
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# Example ...
a = 3
b = 2
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total) 
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Example ...

# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print("Area of Circle = ",area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("Area of Rectangle = ",area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print("Weight of Object = ",weight)

# Calculate the density of a liquid
mass = 75 
volume = 0.075 
density = mass / volume 


# Comparison Operators

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparing something gives either a True or False

print('True == True: ', True == True)    # True
print('True == False: ', True == False)  # False
print('False == False:', False == False) # True

# In addition to the above comparison operator Python uses:

# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)

print("1 is 1 = ", 1 is 2)                    # True - because the data values are the same
print('1 is not 2 = ', 1 is not 2)            # True - because 1 is not 2
print('A in Asabeneh = ', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asabeneh = ', 'B' in 'Asabeneh')  # False - there is no uppercase B
print('coding' in 'coding for all')           # True - because coding for all has the word coding
print('a in an = ', 'a' in 'an')              # True
print('4 is 2 ** 2 = ', 4 is 2 ** 2)          # True

