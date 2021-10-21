
from colorama import Fore
from termcolor import colored
import random 
from time import time

text=["X","O"]

def display():
    print()
    for row in range(3):
        for column in range(3):
            if board[row][column]=='X':
                print(Fore.RED + 'X', end=' ')
                print(Fore.WHITE, end='')
            elif board[row][column]=='O':
                print(Fore.CYAN + 'O', end=' ')
                print(Fore.WHITE, end='')
            else:
                print('-', end=' ')
        print()

def trueposition(x, y):
    if x<=2 and y<=2:
        return True
    else:
        return False

def empty(x, y):
    if board[x][y]=='-':
        return True
    else:
        return False

def gp(name, sign):
    while True:
        print("\nturn : " , name )
        x=int(input("enter row (1 or 2 or 3) : "))
        y=int(input("enter column (1 or 2 or 3) : "))
        x=x-1
        y=y-1
        if trueposition(x, y):
            if empty(x, y):
                board[x][y]=sign
                return
            else:
                print('This position is already filled ! try again...\n')
        else:
            print('This position is illegal ! try again...\n')

def win():

    for i in range(3):
        count_o=0 
        count_x= 0
        for j in range(3):
            test = board[i][j]
            if test=='X':
               count_x+=1
            elif test=='O':
                count_o+=1
        if count_x==3 or count_o==3:
            return True


    for i in range(3):
        count_o=0 
        count_x= 0
        for j in range(3):
            test = board[j][i]
            if test=='X':
                count_x+=1
            elif test=='O':
                count_o+=1
        if count_x==3 or count_o==3:
            return True

    if board[0][0]==board[1][1]==board[2][2] and board[1][1]!='-'  :
        return True

    elif board[0][2]==board[1][1]==board[2][0] and board[1][1]!='-' :
        return True

    return False

def draw():
    for i in range(3):
        for j in range(3):
            if board[i][j]=='-':
                return False
    return True

def check():
    if win():
        return 'win'
    elif draw():
        return 'draw'
    else:
        return 'nothing'

def end(state, name):
    if state=='win':
        print("\n********** winner : ", name, " **********")
    elif state=='draw':
        print('\n******** draw *********\n')

def start(a):
    sign1 = random.choice(text)
    player1 = input('player1 name: ')
    
    if sign1=='O' :
        sign2 = 'X' 
    else :
        sign2='O'
    

    if a=='2' :
         player2 = input('player2 name: ')
    else : 
        player2='bot'


    turn = random.choice(text)

    while True:
        turn = sign1
        display()
        gp(player1, turn)
        test = check()
        if test=='win' or test=='draw':
            display()
            end(test, player1)
            break
        display()
        turn = sign2
        
        if a=='2':
            gp(player2, turn)
        else:
            while True:
                randomrow = random.randint(0, 2)
                randomcolumn = random.randint(0, 2)
                if empty(randomrow, randomcolumn):
                    board[randomrow][randomcolumn]=turn
                    break

        test = check()
        if test=='win' or test=='draw':
            end(test, player2)
            break


while True:
    board = [['-']*3, ['-']*3, ['-']*3]
    menu = input('\n\n**** tic tac toe ****\n\n1.play vs bot\n2.two players\n3.exit\nenter your choice number : ')

    if menu=='1' :
        t1 = time()
        start('1')
        print(" time :" ,round(time() - t1, 2) , "s")
        
    elif menu=='2':
        t1 = time()
        start('2')
        print(" time :" ,round(time() - t1, 2) , "s")
        
    elif menu=='3':
        exit()
