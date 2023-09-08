import replit
import time
from getkey import getkey, keys
from threading import Thread
import random
from colorama import *
import atexit


def cleara():
  print("{}[2J{}[;H".format(chr(27), chr(27)), end="")
  return

def move_to(row,col):
  print("{}[{};{}H".format(chr(27), row, col), end="")
  return

def hide_cursor():
  print('{}[?25l'.format(chr(27)), end="")
  return

def show_cursor():
  print('{}[?25h'.format(chr(27)), end="")
  return

atexit.register(show_cursor)

board = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        8:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        9:[' ','■',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
part1 = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        8:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█','█','█','█',' ',' ',' ',],
        9:[' ',' ',' ',' ',' ',' ','█','█','█','█','█','▲','▲','█','█','█','█','█',' ',' ',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
part2 = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█',' ',' ',' ',' ',' ',],
        8:[' ',' ',' ',' ',' ',' ',' ',' ','█','█','█','█','█',' ','█','█','█',' ',' ',' ',' ',],
        9:[' ',' ',' ','█','█','█','█','█','█','█','█','█','█','▲','█','█','█','█',' ',' ',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
part3 = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█','█',' ',' ',' ',' ',' ',],
        8:[' ',' ',' ',' ',' ',' ',' ',' ','█','█','█','█','█','█','█','█',' ','█',' ',' ',' ',],
        9:[' ',' ',' ','█','█','█','█','█','█','█','█','█','█','█','█','█','▲','█','█',' ',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
part4 = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ',' ',' ',' ',' ','o',' ','█','█','█',' ',' ',' ',' ',' ',],
        8:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█','█',' ','█',' ',' ',' ',],
        9:[' ',' ',' ','█','█','█','█','█','▲','▲','▲','█','█','█','▲','█','█',' ',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
part5 = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▲',' ',' ',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ',' ',' ','o',' ','█','█','█','█','█',' ',' ',' ',' ',' ',],
        8:[' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█','█','█','█',' ','█',' ',' ',' ',],
        9:[' ',' ',' ','█','█','█','▲','▲','▲','█','█','█','█','█','▲','█','█',' ',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
part6 = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▲','▲','▲','▲',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█','█','█',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ',' ',' ','o',' ','█',' ',' ',' ','█','█',' ',' ',' ',' ',],
        8:[' ',' ',' ','█',' ',' ',' ',' ',' ','█','█',' ',' ',' ',' ',' ',' ',' ',' ',],
        9:[' ',' ',' ','█','█','█','▲','▲','▲','█','█','█',' ',' ',' ',' ','▲','▲',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
part7 = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▲','▲','▲',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█','█',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ',' ',' ','o',' ','█',' ',' ',' ','█','█','█','█',' ',' ',],
        8:[' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█','█','█','█','█','█','█','█',' ',],
        9:[' ',' ',' ','█','█','█','▲','▲','▲','█','█','█','█','█','█','█','█','█','█',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
part8 = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█','█','█',' ',' ',' ',],
        7:[' ',' ',' ','█',' ',' ',' ',' ',' ',' ',' ',' ',' ','▼','▼','▼',' ',' ',' ',],
        8:[' ',' ',' ','▼',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','<',' ',' ',' ',],
        9:[' ',' ',' ','>',' ',' ',' ',' ',' ',' ','█','█','█','█','█','█',' ',' ',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
part9 = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ','█','█','█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ','▼','▼','▼',' ','█','█','█',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ','▼','▼','▼',' ','█','█','█',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▼','▼','▼',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ','█','█','█',' ',' ','_',' ',' ',' ',' ',' ',' ',' ',' ',],
        8:[' ',' ',' ',' ',' ','█','█','█',' ','█','█','█',' ',' ',' ',' ',' ',' ',' ',],
        9:[' ',' ',' ','_',' ','█','█','█','▲','█','█','█','▲','█','█','█',' ',' ',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}

y = 9
x = 1
e = 0.075
b = 0
r = 0
score = 0
jump = False
startjump = True
rnd = random.randint(1,3)

def wait(t):
        time.sleep(t)
        
def clear():
        replit.clear()
        
def rnd():
        rnd = random.randint()
        
def move():
        global x, y, jump, b, rnd, r, board, score, jump, e
        rnd = random.randint(1,3)
        cleara()
        hide_cursor()
        while True:
                # time.sleep(10)
                print(f'Score: {score}')
                score += 1
                if board[y+1][x] == ' ' and jump == False:
                        y += 1
                        board[y][x] = ' '
                board[y][x] = f'{Fore.LIGHTGREEN_EX}■{Fore.RESET}'
                move_to(0,0)
                v = 1
                while v != 11:
                        for i in board[v]:
                                if i == '█':
                                        print(i, end = '█')
                                elif i == '▲' or i == '▼':
                                        i = f'{Fore.RED}{i}{Fore.RESET}'
                                        print(i, end = ' ')
                                elif i == 'o' or i == '_':
                                        i = f'{Fore.LIGHTYELLOW_EX}{i}{Fore.RESET}'
                                        print(i, end = ' ')
                                else:
                                        print(i, end = ' ')
                        print('')
                        v += 1
                wait(e)
                if len(board[10]) < 17:
                        board[1].append(' ')
                        board[2].append(' ')
                        board[3].append(' ')
                        board[4].append(' ')
                        board[5].append(' ')
                        board[6].append(' ')
                        board[7].append(' ')
                        board[8].append(' ')
                        board[9].append(' ')
                        board[10].append('█')
                board[y][x] = ' '
                board[1].pop(0)
                board[2].pop(0)
                board[3].pop(0)
                board[4].pop(0)
                board[5].pop(0)
                board[6].pop(0)
                board[7].pop(0)
                board[8].pop(0)
                board[9].pop(0)
                board[10].pop(0)
                if rnd == 1:
                        if b <= 20:
                                board[1].append(part1[1][b])
                                board[2].append(part1[2][b])
                                board[3].append(part1[3][b])
                                board[4].append(part1[4][b])
                                board[5].append(part1[5][b])
                                board[6].append(part1[6][b])
                                board[7].append(part1[7][b])
                                board[8].append(part1[8][b])
                                board[9].append(part1[9][b])
                                board[10].append(part1[10][b])
                        else:
                                rnd = random.randint(1,6)
                                b = 0
                        b += 1
                if rnd == 2:
                        if b <= 20:
                                board[1].append(part2[1][b])
                                board[2].append(part2[2][b])
                                board[3].append(part2[3][b])
                                board[4].append(part2[4][b])
                                board[5].append(part2[5][b])
                                board[6].append(part2[6][b])
                                board[7].append(part2[7][b])
                                board[8].append(part2[8][b])
                                board[9].append(part2[9][b])
                                board[10].append(part2[10][b])
                        else:
                                rnd = random.randint(1,9)
                                b = 0
                        b += 1
                if rnd == 3:
                        if b <= 20:
                                board[1].append(part3[1][b])
                                board[2].append(part3[2][b])
                                board[3].append(part3[3][b])
                                board[4].append(part3[4][b])
                                board[5].append(part3[5][b])
                                board[6].append(part3[6][b])
                                board[7].append(part3[7][b])
                                board[8].append(part3[8][b])
                                board[9].append(part3[9][b])
                                board[10].append(part3[10][b])
                        else:
                                rnd = random.randint(1,9)
                                b = 0
                        b += 1
                if rnd == 4:
                        if b <= 18:
                                board[1].append(part4[1][b])
                                board[2].append(part4[2][b])
                                board[3].append(part4[3][b])
                                board[4].append(part4[4][b])
                                board[5].append(part4[5][b])
                                board[6].append(part4[6][b])
                                board[7].append(part4[7][b])
                                board[8].append(part4[8][b])
                                board[9].append(part4[9][b])
                                board[10].append(part4[10][b])
                        else:
                                rnd = random.randint(1,9)
                                b = 0
                        b += 1
                if rnd == 5:
                        if b <= 18:
                                board[1].append(part5[1][b])
                                board[2].append(part5[2][b])
                                board[3].append(part5[3][b])
                                board[4].append(part5[4][b])
                                board[5].append(part5[5][b])
                                board[6].append(part5[6][b])
                                board[7].append(part5[7][b])
                                board[8].append(part5[8][b])
                                board[9].append(part5[9][b])
                                board[10].append(part5[10][b])
                        else:
                                rnd = random.randint(1,9)
                                b = 0
                        b += 1
                if rnd == 6:
                        if b <= 18:
                                board[1].append(part6[1][b])
                                board[2].append(part6[2][b])
                                board[3].append(part6[3][b])
                                board[4].append(part6[4][b])
                                board[5].append(part6[5][b])
                                board[6].append(part6[6][b])
                                board[7].append(part6[7][b])
                                board[8].append(part6[8][b])
                                board[9].append(part6[9][b])
                                board[10].append(part6[10][b])
                        else:
                                rnd = random.randint(1,9)
                                b = 0
                        b += 1
                if rnd == 7:
                        if b <= 18:
                                board[1].append(part7[1][b])
                                board[2].append(part7[2][b])
                                board[3].append(part7[3][b])
                                board[4].append(part7[4][b])
                                board[5].append(part7[5][b])
                                board[6].append(part7[6][b])
                                board[7].append(part7[7][b])
                                board[8].append(part7[8][b])
                                board[9].append(part7[9][b])
                                board[10].append(part7[10][b])
                        else:
                                rnd = random.randint(1,9)
                                b = 0
                        b += 1
                if rnd == 8:
                        if b <= 18:
                                board[1].append(part8[1][b])
                                board[2].append(part8[2][b])
                                board[3].append(part8[3][b])
                                board[4].append(part8[4][b])
                                board[5].append(part8[5][b])
                                board[6].append(part8[6][b])
                                board[7].append(part8[7][b])
                                board[8].append(part8[8][b])
                                board[9].append(part8[9][b])
                                board[10].append(part8[10][b])
                        else:
                                rnd = random.randint(1,9)
                                b = 0
                        b += 1
                if rnd == 9:
                        if b <= 18:
                                board[1].append(part9[1][b])
                                board[2].append(part9[2][b])
                                board[3].append(part9[3][b])
                                board[4].append(part9[4][b])
                                board[5].append(part9[5][b])
                                board[6].append(part9[6][b])
                                board[7].append(part9[7][b])
                                board[8].append(part9[8][b])
                                board[9].append(part9[9][b])
                                board[10].append(part9[10][b])
                        else:
                                rnd = random.randint(1,9)
                                b = 0
                        b += 1
                if board[y][x] == '█' or board[y][x] == '▲' and jump == False or board[y+1][x-1] == '▲' and jump == False or board[y][x] == '▼':
                        print('\nFail')
                        startjump = False
                        break
                elif board[y][x] == '>':
                        e -= 0.025
                elif board[y][x] == '<':
                        e += 0.025
                if board[y][x] == '_':
                        jumpy2 = Thread(target=jpad)
                        jumpy2.setDaemon(True)
                        jumpy2.start()
        show_cursor()
        e = 0.075
        print('Hold [Enter] to try again!')
        startjump = True
        key = getkey()
        replit.clear()
        board = {
        1:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        2:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        3:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        4:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        5:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        6:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        7:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        8:[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
        9:[' ','■',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
       10:['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█',],
}
        b = 0
        score = 0
        rnd = random.randint(1,4)
        go = Thread(target=move)
        jumpy = Thread(target=jcheck)
        jumpy.setDaemon(True)   
        go.setDaemon(True)   
        go.start()
        play()

go = Thread(target=move)
go.setDaemon(True)   
go.start()

def jpad():
        global y, x
        jump = True
        board[y][x] = ' '
        board[y-3][x] = f'{Fore.LIGHTGREEN_EX}■{Fore.RESET}'
        y -= 3
        if board[y][x] == 'o' or board[y+1][x] == 'o' or board[y][x+1] == 'o' or board[y-1][x] == 'o' or board[y][x-1] == 'o' or board[y+1][x+1] == 'o' or board[y-1][x-1] == 'o' or board[y+1][x-1] == 'o' or board[y-1][x+1] == 'o':
                try:
                        jumpy = Thread(target=jcheck)
                        jumpy.setDaemon(True)
                        jumpy.start()
                except:
                        pass
        wait(e)
        board[y][x] = ' '
        board[y-3][x] = f'{Fore.LIGHTGREEN_EX}■{Fore.RESET}'
        y -= 3
        if board[y][x] == 'o' or board[y+1][x] == 'o' or board[y][x+1] == 'o' or board[y-1][x] == 'o' or board[y][x-1] == 'o' or board[y+1][x+1] == 'o' or board[y-1][x-1] == 'o' or board[y+1][x-1] == 'o' or board[y-1][x+1] == 'o':
                try:
                        jumpy = Thread(target=jcheck)
                        jumpy.setDaemon(True)
                        jumpy.start()
                except:
                        pass
        wait(e)
        while board[y+1][x] != '█' and board[y+1][x+1] != '█':
                board[y][x] = ' '
                board[y+1][x] = f'{Fore.LIGHTGREEN_EX}■{Fore.RESET}'
                y += 1
                if board[y][x] == 'o' or board[y+1][x] == 'o' or board[y][x+1] == 'o' or board[y-1][x] == 'o' or board[y][x-1] == 'o' or board[y+1][x+1] == 'o' or board[y-1][x-1] == 'o' or board[y+1][x-1] == 'o' or board[y-1][x+1] == 'o':
                        try:
                                jumpy = Thread(target=jcheck)
                                jumpy.setDaemon(True)
                                jumpy.start()
                        except:
                                pass
                wait(e)
        jump = False
        play()

def jcheck():
        jumpy = Thread(target=jcheck)
        jumpy.setDaemon(True)
        key = getkey()
        if key == keys.SPACE:
                play()
                
jumpy2 = Thread(target=jpad)
jumpy2.setDaemon(True)

jumpy = Thread(target=jcheck)
jumpy.setDaemon(True)   

def play():
        global y, x, jump, board, startjump
        if startjump == True:
                key = getkey()
                if key == keys.SPACE:
                        jump = True
                        board[y][x] = ' '
                        board[y-1][x] = f'{Fore.LIGHTGREEN_EX}■{Fore.RESET}'
                        y -= 1
                        if board[y][x] == 'o' or board[y+1][x] == 'o' or board[y][x+1] == 'o' or board[y-1][x] == 'o' or board[y][x-1] == 'o' or board[y+1][x+1] == 'o' or board[y-1][x-1] == 'o' or board[y+1][x-1] == 'o' or board[y-1][x+1] == 'o':
                                try:
                                        jump2 = False
                                        jumpy = Thread(target=jcheck)
                                        jumpy.setDaemon(True)
                                        jumpy.start()
                                except:
                                        pass
                        wait(e)
                        board[y][x] = ' '
                        board[y-1][x] = f'{Fore.LIGHTGREEN_EX}■{Fore.RESET}'
                        y -= 1
                        if board[y][x] == 'o' or board[y+1][x] == 'o' or board[y][x+1] == 'o' or board[y-1][x] == 'o' or board[y][x-1] == 'o' or board[y+1][x+1] == 'o' or board[y-1][x-1] == 'o' or board[y+1][x-1] == 'o' or board[y-1][x+1] == 'o':
                                try:
                                        jump2 = False
                                        jumpy = Thread(target=jcheck)
                                        jumpy.setDaemon(True)
                                        jumpy.start()
                                except:
                                        pass
                        wait(e)
                        jump2 = True
                        while board[y+1][x] != '█' and board[y+1][x+1] != '█':
                                if jump2 == True:
                                        board[y][x] = ' '
                                        board[y+1][x] = f'{Fore.LIGHTGREEN_EX}■{Fore.RESET}'
                                        y += 1
                                        if board[y][x] == 'o' or board[y+1][x] == 'o' or board[y][x+1] == 'o' or board[y-1][x] == 'o' or board[y][x-1] == 'o' or board[y+1][x+1] == 'o' or board[y-1][x-1] == 'o' or board[y+1][x-1] == 'o' or board[y-1][x+1] == 'o':
                                                try:
                                                        jump2 = False
                                                        jumpy = Thread(target=jcheck)
                                                        jumpy.setDaemon(True)
                                                        jumpy.start()
                                                except:
                                                        pass
                                        wait(e)
                        jump2 = True
                        jump = False
        play()
play()