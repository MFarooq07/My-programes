"""
Created by: Muhammad Farooq Memon
Role: Student
Institute: Union College
"""
import random


def elec_dice():
    """
    The following function rolls a dice for any dice game and shows the number as on the real dice.
    :return: nothing
    """
    a = 0
    while a != 1:
        dice_num = random.randint(1,6)
        print(dice_num)
        if dice_num == 1:
            print("_ _ _\n   \n  0  \n   \n_ _ _")
        elif dice_num == 2:
            print("_ _ _\n    0\n0    \n_ _ _")
        elif dice_num == 3:
            print("_ _ _\n    0\n  0  \n0    \n_ _ _")
        elif dice_num == 4:
            print("_ _ _\n0   0\n   \n0   0\n_ _ _")
        elif dice_num == 5:
            print("_ _ _\n0   0\n  0  \n0   0\n_ _ _")
        else:
            print("_ _ _\n0 0 0\n   \n0 0 0\n_ _ _")



        input("press enter to throw the dice")



if __name__ == "__main__":
    elec_dice()

