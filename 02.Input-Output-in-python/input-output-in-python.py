
# with print() function, we can display output in various formats, while input() function enables us to gather
# input from the user during program execution.


# -- Taking Input in python :
# Python input() function is used to take user input. By default it returns the user input in the form of a string.

# name = input("Enter your name :")
# print("Hello ,", name,"!")


# -- Printing Variables : 
# we can use the print() funtion to print single or multiple variables, we can print multiple variables in a single
# line by sperating them with comma (,)

# # Single Variable : 
# std = "Jhon"
# print(std)

# # multiple Variables :
# std = "Wick"
# age = 25
# city = "London"
# print(std, age, city)


# -- Take multiple inputs in python : 
# We are taking multiple inputs from the user by using the split() method. split() function can split the values
# entered by user into separate variables.

# x, y = input("Enter two values = ").split()
# print("Number of boys : ", x)
# print("Number of girls : ", y)

# x,y,z = input("Enter three values = ").split()
# print("Number of Children : ", x)
# print("Number of boys : ", y)
# print("Number of girls : ", z)


# -- Take Conditional Input from user in Python
# the program prompts the user to enter their age. The input is converted to an integer using the int() function.

# age_input = input("Enter your age : ")
# age = int(age_input)

# if age < 0 :
#     print("Enter a valid age!")

# elif age < 18 :
#     print("You are a minor")

# elif age >= 18 and age < 65 :
#     print("You are an adult")

# else:
#     print("You are a senior citizen")
    
    
# -- How to Change the Type of Input in Python :

# Print name in python :
# color = input("Color of rose is : ")
# print(color)

# # print number in python :
# num = int(input("How many roses : "))
# print(num)

# # print float/decimal number in python : 
# price = float(input("Price of each rose : "))
# print(price)


# -- Find DataType of Input in Python

# a = "Hello World"
# b = 10
# c = 11.22
# d = ("Geeks", "for", "Geeks")
# e = ["Geeks", "for", "Geeks"]
# f = {"Geeks": 1, "for":2, "Geeks":3}

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))


# -- Output Formatting :

# 1. Using Format()
# amount = 175.6764
# print("Amount : ${:.3f}".format(amount))


# 2. Using sep and end parameter

# # end Parameter with '@'
# print("Python", end='@')
# print("GeeksforGeeks")

# # Seprating with Comma
# print('G', 'F', 'G', sep='')

# # for formatting a date
# print('09', '12', '2016', sep='-')

# # another example
# print('pratik', 'geeksforgeeks', sep='@')


# 3. Using f-string

# name = "Jhon"
# age = 23
# print(f"Hello my name is {name} and I'm {age} years old")


# 4. Using % Operator

# Taking input from the user
num = int(input("Enter a value: "))
add = num + 5
print("The sum is %d" %add)