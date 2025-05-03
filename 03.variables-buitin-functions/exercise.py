
# 1. Check the data type of all your variables using type() built-in function

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(skills))
print(type(person_info))


# 2. Using the len() built-in function, find the length of your first name

print(len(first_name))


# 3 . Compare the length of your first name and your last name

print("Length of First Name = ", len(first_name))
print("Length of Last Name = ", len(last_name))


# 4. Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

add = num_one + num_two      # Addition 
sub = num_one - num_two      # Subtraction 
mul = num_one * num_two      # Multiplication 
div = num_one / num_two      # Division 
rem = num_one % num_two     # Remainder 
pow_of = num_one ^ num_two   # Power Of

print(add)
print(sub)
print(mul)
print(div)
print(rem)
print(pow_of)


# 5. The radius of a circle is 30 meters.
# i. Calculate the area of a circle and assign the value to a variable name of area_of_circle

rad = 30
area_of_circle = float(3.14 * pow(rad, 2))
print("Area of circle is = ", str(area_of_circle))

# ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

circum_of_circle = 2 * 3.14 * rad
print("Circumference of circle is = ", circum_of_circle)

# iii. Take radius as user input and calculate the area.

input_radius = float(input("Enter the radius : "))
area = float(3.14 * pow(input_radius, 2))
print("Area of circle is = ", str(area))


# 6. Use the built-in input function to get first name, last name, age
# from a user and store the value to their corresponding variable names

# first_name = input("Enter First Name : ")
# last_name = input("Enter Last Name : ")
# age = input("Enter Age : ")

print(first_name)
print(last_name)
print(age)

 