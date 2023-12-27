import math
import random

firstDice = 0
secondDice = 0

def roll():
    firstDice = int(random.randrange(1, 7))
    print(f"The value of Die 1 is {firstDice}")
    secondDice = int(random.randrange(1, 7))
    print(f"The value of Die 2 is {secondDice}")

print("A roll of the dice:")
roll()