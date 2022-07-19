import random


def toss():
    """
    The following program tosses a coin for the user and tells whether the user has won or lost the toss.
    :return: nothing
    """
    toss_poss = ["HEADS", "TAILS"]
    reset_toss = 0
    while reset_toss != 2:
        user_demand = input("Please enter:\n 1 for Heads \n 2 for Tails")# cut it to later in the code
        coin_face = random.randint(0,1)
        user_win = compare_call(user_demand, coin_face + 1)
        if user_win:
            print("Its ", toss_poss[int(user_demand) - 1], "Your call")
        else:
            print("Its not ", toss_poss[int(user_demand) - 1])

        reset_toss = input("Do you want to toss again?\n 1 for YES\n 2 for NO")


def compare_call(user_demand, coin_face):

    if int(user_demand) == coin_face:
        return True
    else:
        return False

if __name__ == "__main__":
    toss()
    print("Press green play button on the left to play again\n           THANK YOU FOR YOUR TIME            ")