import random
while True:
    yourChoice = input("enter your choice: y/n ")


    if yourChoice == "y":
        firstDie = random.randint(1,6)
        secondDie = random.randint(1,6)
        print(f'({firstDie}, {secondDie})')
        
    elif yourChoice == "n":
        print("thanks for not playing :)")
        break
    else: 
         print("invalid game")
         

