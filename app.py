# from converters import kg_to_lb

# s = kg_to_lb(70)
# print(s)


# import utils
# numbers = [30, 20, 4, 50]
# max = utils.find_max(numbers)
# print(max)


# import random

# listt = ["shrawan", "dipisha", "1", "2", "Leo messi"]
# leader = random.choice(listt)
# print(leader)

# import random


# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         third = random.randint(2, 7)
#         return first, second, third
    

# dice = Dice()
# print(dice.roll())

from pathlib import Path

path = Path()
for file in path.glob('*'):
    print(file)

