import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter a choice : ")

youdict = {"s":1,"w":-1,"g":0}
reversedict = {1:"snake",-1:"water",0:"gun"}

you = youdict[youstr]

print(f"you chose {reversedict[you]} and computer chose {reversedict[computer]}")

if(computer == you):
    print("match is draw")
else:

    """
    if(you == 1 and computer == 0):   1
        print("You Lose!")
    elif(you == 1 and computer == -1): 2 
        print("You Win!")
    elif(you == 0 and computer == -1): 1
        print("You Lose!")
    elif(you == 0 and computer == 1): -1
        print("You Win!")
    elif(you == -1 and computer == 1):  -2
        print("You Lose!")
    elif(you == -1 and computer == 0): -1
        print("You Win!")
    else:
        print("something went wrong")
    """
     
    # The below logic is written on the basis of the value of (you - computer)
    
    if(((you - computer) == 1) or ((you - computer) == -2)):   
        print("you lose !")
    else:
        print("you win") 