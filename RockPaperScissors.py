import random


def rps():
    """
    The following function plays the rock,paper and scissor game for the user and displays the score at the point
    when the user loses or the user does not want to proceed the game any further.
    :return: nothing
    """
    user_choice = input("Please enter\n 1. for rock \n 2. for paper \n 3. for scissors \n 4. for ending the game")
    game_over = False
    total_score = 0
    option_game = ["rock", "paper", "scissor"]

    while not game_over:
        comp_choice = random.randrange(1, 4)
        print(comp_choice)
        print(option_game[comp_choice - 1])

        if int(user_choice) == 4:
            game_over = True
        elif int(user_choice) == comp_choice:
            print("\nIts a TIE!!!! :| \n")
        elif (int(user_choice) == 3 and comp_choice == 2) or (int(user_choice) == 2 and comp_choice == 1) or (
                int(user_choice) == 1 and comp_choice == 3):
            print("\nYou WON :)\n")
            total_score += 1
        else:
            print("\nYou LOST :(\n")
            game_over = True
        if not game_over:
            user_choice = input(
                "\nPlease enter\n 1. for rock \n 2. for paper \n 3. for scissors \n 4. for ending the game")

    print("YOUR SCORE:", total_score)


if __name__ == "__main__":
    rps()
