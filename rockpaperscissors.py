# rock paper scissors
"""
STUDY
p1/p2
#r-r=0, draw
#r-p=-2 and p1==r, p2 wins
r-s=-4, p1 wins
#p-p=0, draw
p-r=2 and p1==p, p1 wins
#p-s=-2 and p1==p, p2 wins
#s-s=0, draw
s-r=4, p2 wins
s-p=2, and p1==s, p1 wins
"""

import random
import sys

hand = ['r', 'p', 's']
cscor = 0  # computer score
pscor = 0  # player score

# draw: rr, ss, pp
# p1 wins: sp, rs, pr
# c wins: ps, sr, rp

def calculate_winner(player, computer):
    if player == computer:
        return "draw"
    elif (computer == "r" and player == 's') or (computer == "p" and player == 'r') or (computer == "s" and player == 'p'):
        return "computer"
    else:
        return "player"

def loop():
    global cscor, pscor
    p1_choice = input("player 1: ")
    comp_choice = random.choice(hand)
    print('computer:', comp_choice)

    winner = calculate_winner(p1_choice, comp_choice)

    if winner == "draw":
        print("draw\n")
    elif winner == "computer":
        cscor = cscor + 1
        print("computer wins\ncomputer:", cscor, "\nplayer 1:", pscor, "\n")
    else:
        pscor = pscor + 1
        print("player 1 wins\ncomputer:", cscor, "\nplayer 1:", pscor, "\n")

    loop()

def bestof3(pscor, cscor):
    p1_choice = input("player 1: ")
    comp_choice = random.choice(hand)
    print('computer:', comp_choice)

    winner = calculate_winner(p1_choice, comp_choice)
    
    if winner == "draw":
        pass
    elif winner == "computer":
        cscor = cscor + 1
    else:
        pscor = pscor + 1
        
    if cscor==2 or pscor==2:
        if cscor==2:
            print('computer wins!')
        else:
            print('player 1 wins!')

        if input('wanna play again? (y/n) ') == "y":
            bestof3(0, 0)
        else:
            sys.exit()
    bestof3(pscor, cscor)

game_mode = input(
    "welcome to the rock-paper-scissors game\n"
    'instructions: enter "r" for rock, "p" for paper, and "s" for scissors\n\n'
    "for eternity game, type -> 1\nfor best of 3, type -> 2\n"
)

if game_mode == "1":
    loop()
elif game_mode == "2":
    bestof3(0, 0)
else:
    print("invalid entry, run script again")