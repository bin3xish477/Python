'''
role a dice
Alexis Rodriguez
12 July 2019
'''
import random
print("Welcome to my simulated roll of dice!")
MIN = 1
MAX = 6
roll_dice = "yes"
while roll_dice == "yes" or roll_dice == "y":
    print("Your values are: ")
    print(random.randint(MIN, MAX))
    print(random.randint(MIN, MAX))
    roll_dice = input("Do you want to roll again? if you do, type yes or y: ")
