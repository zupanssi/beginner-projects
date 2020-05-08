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

d = {"r": 0, "p": 2, "s": 4}
hand = [0, 2, 4]
cscor = 0  # computer score
pscor = 0  # player score

def computer_chooses():
    comp_choice = random.choice(hand)
    if comp_choice == 0:
        print("computer: r")
    elif comp_choice == 2:
        print("computer: p")
    elif comp_choice == 4:
        print("computer: s")
    return comp_choice

def loop():
    global cscor, pscor
    p1_choice = d[input("player 1: ")]
    comp_choice = computer_chooses()

    if p1_choice - comp_choice == 0:
        print("draw\n")
    elif p1_choice - comp_choice == 4 or p1_choice - comp_choice == -2 and p1_choice < 4:
        cscor = cscor + 1
        print("computer wins\ncomputer:", cscor, "\nplayer 1:", pscor, "\n")
    else:
        pscor = pscor + 1
        print("player 1 wins\ncomputer:", cscor, "\nplayer 1:", pscor, "\n")
    loop()

def bestof3(pscor, cscor):
    p1_choice = d[input("player 1: ")]
    comp_choice = computer_chooses()

    if p1_choice - comp_choice == 4 or p1_choice - comp_choice == -2 and p1_choice < 4:
        cscor = cscor + 1
    else:
        pscor = pscor + 1
    if cscor==2:
        r = input("computer wins!\nplay again? (y/n) ")
        if r == "y":
            bestof3(0, 0)
        else:
            sys.exit()
    if pscor==2:
        r = input("player 1 wins!\nplay again? (y/n) ")
        if r == "y":
            bestof3(0, 0)
        else:
            sys.exit()
    bestof3(pscor, cscor)

s = input(
    "welcome to the rock-paper-scissors game\n"
    'instructions: enter "r" for rock, "p" for paper, and "s" for scissors\n\n'
    "for eternity game, type -> 1\nfor best of 3, type -> 2\n"
)

if s == "1":
    loop()
elif s == "2":
    bestof3(0, 0)
else:
    print("invalid entry, run script again")
