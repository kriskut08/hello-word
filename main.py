"""
/----------------------------\
| Tic Tac Toe v4.1 (*^_^*)
|
| ▛▀▀▀▀▀▀▀▜
| ▌ X - - ▐
| ▌ O O - ▐
| ▌ - - X ▐
| ▙▃▃▃▃▃▃▃▟
|
\------------------------------/
"""
from colorama import *
init(autoreset=True)


lap = 0
charD = [Fore.RED + "X", Fore.BLUE + "O"]
char = [Fore.RED + "X", Fore.BLUE + "O"]
game = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]
def PrintBoard():
    print('\u259B▀▀▀▀▀▀▀\u259C')
    for i in range(len(game)):
        for j in range(len(game)):
            if (j==0):
                print("▌ " + game[i][j], end=' ')
            else:
                print(game[i][j], end=' ')
        print("▐")
    print('\u2599▄▄▄▄▄▄▄\u259F')

def Check():
    if (game[0][0] + game[0][1] + game[0][2] == charD[0]*3): return "r"
    if (game[0][0] + game[0][1] + game[0][2] == charD[1]*3): return "b"

    if (game[1][0] + game[1][1] + game[1][2] == charD[0]*3): return "r"
    if (game[1][0] + game[1][1] + game[1][2] == charD[1]*3): return "b"

    if (game[2][0] + game[2][1] + game[2][2] == charD[0]*3): return "r"
    if (game[2][0] + game[2][1] + game[2][2] == charD[1]*3): return "b"

    if (game[0][0] + game[1][0] + game[2][0] == charD[0]*3): return "r"
    if (game[0][0] + game[1][0] + game[2][0] == charD[1]*3): return "b"

    if (game[0][1] + game[1][1] + game[2][1] == charD[0]*3): return "r"
    if (game[0][1] + game[1][1] + game[2][1] == charD[1]*3): return "b"

    if (game[0][2] + game[1][2] + game[2][2] == charD[0]*3): return "r"
    if (game[0][2] + game[1][2] + game[2][2] == charD[1]*3): return "b"

    if (game[0][0] + game[1][1] + game[2][2] == charD[0]*3): return "r"
    if (game[0][0] + game[1][1] + game[2][2] == charD[1]*3): return "b"

    if (game[2][0] + game[1][1] + game[0][2] == charD[0]*3): return "r"
    if (game[2][0] + game[1][1] + game[0][2] == charD[1]*3): return "b"

def IsDraw():
    if (str(game[0][0] + game[0][1] + game[0][2]+ game[1][0] + game[1][1] + game[1][2] + game[2][0] + game[2][1] + game[2][2]).__contains__("-")):
        return False
    else:
        return True

def Game():
    while True:
        if (not IsDraw()):
            choice = input("hova tegyem?")
            if (choice.__contains__(":")):
                x = int(choice[0]) - 1
                y = int(choice[2]) - 1
            if (game[x][y] == "-"):
                game[x][y] = char[0]
                temp = char[0]
                char[0] = char[1]
                char[1] = temp
                if (Check()=="b"):
                    print(Fore.BLUE +"A kék nyert!")
                    PrintBoard()
                    break
                elif (Check()=="r"):
                    print(Fore.RED + "A piros nyert!")
                    PrintBoard()
                    break
                else:
                    PrintBoard()
        else:
            print("Döntetlen!")
            break
Game()