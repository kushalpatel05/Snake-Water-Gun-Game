# In this game ,Snake beats Water (Snake drinks Water), Water beats Gun (Gun drowns in water), and Gun beats Snake (Gun shoots the snake).

'''
1 for Snake
-1 for Water
0 for Gun
'''
import random

# Computer randomly selects a value from -1, 0, or 1
Computer = random.choice([-1,0,1])


youstr = input("Enter your choice from S(Snake), W(Water), G(Gun): ")

youdict = {"S" : 1,"W" : -1,"G" : 0}      #Both dictionaries are connected with each other..
reversedict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

# Convert user input to corresponding numeric value
you = youdict[youstr]

# By now, we have 2 numbers (variables), you and computer 
print(f"You chose {reversedict[you]} \nComputer chose {reversedict[Computer]}")

# If both choices are the same, it's a draw
if(Computer == you):
    print("Match is a draw..")

else:
    # Check all winning and losing conditions based on combinations
    if(Computer == -1 and you == 1 ):
        print("You Win...")

    elif(Computer == -1 and you == 0):
        print("You Lose...")

    elif(Computer == 0 and you == -1):
        print("You win...")

    elif(Computer == 0 and you == 1):
        print("You Lose...")

    elif(Computer == 1 and you == -1):
        print("You Lose...")

    elif(Computer == 1 and you == 0):
        print("You Win...")
    
    else:
        print("Something went wrong.") # We’ll know if something is wrong.
