
# # Variables in Python

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# country = 'Finland'
# city = 'Helsinki'
# age = 250
# is_married = True
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#    'firstname':'Asabeneh',
#    'lastname':'Yetayeh',
#    'country':'Finland',
#    'city':'Helsinki'
#    }

# print(type(first_name))
# print(type(age))
# print(type(is_married))
# print(type(skills))
# print(type(person_info))


# print('Hello, World!') # The text Hello, World! is an argument
# print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
# print(len('Hello, World!')) # it takes only one argument


# # Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)


# # Declaring Multiple Variable in a Line

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)


# # Checking Data types and Casting

# first_name = 'Asabeneh'     # str
# last_name = 'Yetayeh'       # str
# country = 'Finland'         # str
# city= 'Helsinki'            # str
# age = 250                   # int, it is not my real age, don't worry about it

# # Printing out types
# print(type('Asabeneh'))     # str
# print(type(first_name))     # str
# print(type(10))             # int
# print(type(3.14))           # float
# print(type(1 + 1j))         # complex
# print(type(True))           # bool
# print(type([1, 2, 3, 4]))     # list
# print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
# print(type((1,2)))                                              # tuple
# print(type(zip([1,2],[3,4])))                                   # set

# # Casting : Converting one data type to another data type.

# # int to float
# num_int = 10
# print("int = ", num_int)          # 10
# num_float = float(num_int)
# print("float = ", num_float)      # 10.0

# # float to int
# gravity = 9.81
# print(int(gravity))                # 9

# # int to str
# num_int = 10
# num_str = str(num_int)
# print(num_str)                     # '10'

# # str to int or float
# num_str = '10.6'
# print('num_int', int(num_str))      # 10
# print('num_float', float(num_str))  # 10.6

# # str to list

# first_name = "Hamza"
# print(first_name)         # Hamza
# print(list(first_name))   # ['H', 'a', 'm', 'z', 'a']


# # Getting user input using the input() built-in function

# first_name = input('What is your name: ')
# age = input('How old are you? ')

# print(first_name)
# print(age)



# ............_________________................

# -- Python variables:
# In python, a variable is used to store data that can be referenced and manipulated during program execution.

x = 5   # variable x stores the integer value 5
name =  "samantha"  # variable name stores a string value samantha

print(x)
print(name)


# -- Assigning values to a variable

# Basic Assignment : 
# Variables in python are aissgned values using the = operator
x = 5
# y = 3.14
z = "Hi"

# Dynamic Typing :
# Python variables are dynamically typed, meaning the same variable can hold different types of value during
# execution.
x = 10
x = "Hello world"

# Multile Assignment :
# Python allow to assign multiple variables in a single line, also python allows to assign same value to 
# multiple varaibles
a = b = c = 100
print(a, b, c)

# Assigning different values :
# We can assign different values to multiple variables in a single line
# x, y, z = 11, 3.14, "Hashim"
# print(x, y, z)


# -- Type casting a variable : 
# Type casting refers to the process of converting the value of one data type to another 

# Basic casting functions :
# - int() : convert values to integer values
# - float() : transform values to floating point number 
# - str() : convert values to strings
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string 

# Display results
print(n)  
print(f)  
print(s2)  


# -- Scope of variable : 
# There are two types of scope for defigning a variable in python :

# - Local Scope :
# variable defined inside a function are local to that function :
# def f():
#    a = "I am local"
#    print(a)
# f()

# - Global Scope :
# Variable defined outside the function are global and can be accessed inside the function using global keyword.
# a = "I am global"
# def f():
#    global a
#    a = "Modified globally"
#    print(a)
# f()
# print(a)


# --Practical Examples
# Swapping Two Variables :
x = 3
y = 7
x, y = y, x
print(x, y)

a = 5
b = 10
a = b
b = a
print(a)
print(b)


# Counting Characters in a String
word = "Python"
length = len(word)
print("Length of word : ", length)