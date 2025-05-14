# Loops in python are used to repeat actions effeciently.

# --- While Loop
# A while loops is used to execute the block of code of statement repeatedly until the given condition is satisfied.
# when the condition becomes false, the line immediately after the loop in program is executed.

# Example : 
num = 0
while (num < 3):
    num = num + 1
    print("Hello")
    
    
# - The break Statement
# With the break statement we can stop the loop even if the while condition is true:
val = 0 
while (val < 6):
    val = val + 1
    print(val)
    if val == 4:
        break
    
# - The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while(i < 7):
    i = i + 1
    print(i)
    if i == 4:
        continue
    i = i + 1
