# rock paper scissors

import random
import sys

hand = ["r", "p", "s"]
cscore, pscore = 0, 0


def calculate_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (computer == "r" and player == "s")
        or (computer == "p" and player == "r")
        or (computer == "s" and player == "p")
    ):
        return "computer"
    else:
        return "player"


def eternity():
    global cscore, pscore
    p1_choice = input("player 1: ")
    comp_choice = random.choice(hand)
    print("computer:", comp_choice)

    winner = calculate_winner(p1_choice, comp_choice)

    if winner == "draw":
        print("\ndraw.\n")
    elif winner == "computer":
        cscore = cscore + 1
        print("\ncomputer wins.\n")
    else:
        pscore = pscore + 1
        print("\nplayer 1 wins.\n")

    print("computer:", cscore, "\nplayer 1:", pscore, "\n")

    eternity()


def bestof3(pscore, cscore):
    p1_choice = input("player 1: ")
    comp_choice = random.choice(hand)
    print("computer:", comp_choice)

    winner = calculate_winner(p1_choice, comp_choice)

    if winner == "draw":
        pass
    elif winner == "computer":
        cscore = cscore + 1
    else:
        pscore = pscore + 1

    if cscore == 2 or pscore == 2:
        if cscore == 2:
            print("\ncomputer wins!")
        else:
            print("\nplayer 1 wins!")

        if input("wanna play again? (y/n) ") == "y":
            bestof3(0, 0)
        else:
            sys.exit()
    bestof3(pscore, cscore)


game_mode = input(
    "welcome to the rock-paper-scissors game\n"
    'instructions: enter "r" for rock, "p" for paper, and "s" for scissors\n\n'
    "for eternity game, type -> 1\nfor best of 3, type -> 2\n"
)

if game_mode == "1":
    eternity()
elif game_mode == "2":
    bestof3(0, 0)
else:
    print("invalid entry, run script again")
