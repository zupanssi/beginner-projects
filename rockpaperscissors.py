#rock paper scissors
'''
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
'''

import random
import sys
d={'r':0,'p':2,'s':4}
c=[0,2,4]
cscor=0 #computer score
pscor=0 #player score

def loop():
    random.shuffle(c)
    a=int(d[input('player 1: ')])
    b=int(c[0])
    global cscor,pscor
    if b==0:
        print('computer: r')
    elif b==2:
        print('computer: p')
    elif b==4:
        print('computer: s')
        
    if a-b==0:
        print('draw\n')
    elif a-b==4 or a-b==-2 and a<4:
        print('computer wins\ncomputer:',cscor+1,
        '\nplayer 1:',pscor,'\n')
        cscor=cscor+1
    else:
        print('player 1 wins\ncomputer:',cscor,
        '\nplayer 1:',pscor+1,'\n')
        pscor=pscor+1
    loop()

def r0():
    random.shuffle(c)
    a=int(d[input('player 1: ')])
    b=int(c[0])
    if b==0:
        print('computer: r')
    elif b==2:
        print('computer: p')
    elif b==4:
        print('computer: s')
    if a-b==0:
        r0()
    elif a-b==4 or (a-b==-2 and a<4):
        r2()
    else:
        r1()

def r1():
    random.shuffle(c)
    a=int(d[input('player 1: ')])
    b=int(c[0])
    if b==0:
        print('computer: r')
    elif b==2:
        print('computer: p')
    elif b==4:
        print('computer: s')
        
    if a-b==0:
        r1()
    elif a-b==4 or (a-b==-2 and a<4):
        r3()
    else:
        r=input('player 1 wins!\nplay again? (y/n) ')
        if r=='y':
            r0()
        else:
            sys.exit()

def r2():
    random.shuffle(c)
    a=int(d[input('player 1: ')])
    b=int(c[0])
    if b==0:
        print('computer: r')
    elif b==2:
        print('computer: p')
    elif b==4:
        print('computer: s')
        
    if a-b==0:
        r2()
    elif a-b==4 or (a-b==-2 and a<4):
        r=input('computer wins!\nplay again? (y/n) ')
        if r=='y':
            r0()
        else:
            sys.exit()
    else:
        r3()
        
def r3():
    random.shuffle(c)
    a=int(d[input('player 1: ')])
    b=int(c[0])
    if b==0:
        print('computer: r')
    elif b==2:
        print('computer: p')
    elif b==4:
        print('computer: s')
        
    if a-b==0:
        r3()
    elif a-b==4 or (a-b==-2 and a<4):
        r=input('computer wins!\nplay again? (y/n) ')
        if r=='y':
            r0()
        else:
            sys.exit()
    else:
        r=input('player 1 wins!\nplay again? (y/n) ')
        if r=='y':
            r0()
        else:
            sys.exit()

s=input('welcome to the rock-paper-scissors game\n'
        'instructions: enter "r" for rock, "p" for paper, and "s" for scissors\n\n'
        'for eternity game, type -> 1\nfor best of 3, type -> 2\n')

if s=='1':
    loop()
elif s=='2':
    r0()
else:
    print('invalid entry, run script again')

