import random    
compNum = random.randint(1, 100)

while True:
    try:
        userNum = int(input("Guess a number between 1 and 100 : "))
    except ValueError:
        print("Please enter a valid number")
        
    if userNum > compNum:
        print("Too High!")
    elif userNum < compNum:
        print("Too Low!")
    else:
        print("Congratulations... You Guess Right!")
        break