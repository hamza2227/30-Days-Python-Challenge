# # --- Conditional Statements in python are used to execute certain blocks of code based on specific condition.

# - If Conditional Statement : 
age = 20
if age >= 18:
    print("Eligible to vote")
    
    
# - If else Conditional Statements :
age = 12
if age <= 10:
    print("Travel for free!")
else:
    print("Pay the Ticket")
    
    
# - elif Statement :
age = 25
if age <= 12:
    print("Child")
elif age <=19:
    print("Teenager")
elif age <=35:
    print("Young Adult")
else:
    print("Adult")
    
    
# - Nested if..else Conditional Statements :
age = 41
if age >= 12:
    print("Above 12")
    if age >= 19:
        print("Above 19 also")
    if age >= 25:
        print("Above 25 also")
else:
    print("Kid")    
    

# - Match-Case Statement :
number = 3
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
