import tkinter
from tkinter import Tk

root = Tk()
root.geometry("550x570")
root.title("TicTacToe")
root.iconbitmap('file-49-512.ico')

charD = ["X", "O"]
pl = ["X", "O"]
game = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]


class Button:
    def __init__(self, row, col, size, char):
        self.row = row
        self.col = col
        self.sze = size
        self.char = char

        def Check():
            if (game[0][0] + game[0][1] + game[0][2] == charD[0] * 3): return "r"
            if (game[0][0] + game[0][1] + game[0][2] == charD[1] * 3): return "b"

            if (game[1][0] + game[1][1] + game[1][2] == charD[0] * 3): return "r"
            if (game[1][0] + game[1][1] + game[1][2] == charD[1] * 3): return "b"

            if (game[2][0] + game[2][1] + game[2][2] == charD[0] * 3): return "r"
            if (game[2][0] + game[2][1] + game[2][2] == charD[1] * 3): return "b"

            if (game[0][0] + game[1][0] + game[2][0] == charD[0] * 3): return "r"
            if (game[0][0] + game[1][0] + game[2][0] == charD[1] * 3): return "b"

            if (game[0][1] + game[1][1] + game[2][1] == charD[0] * 3): return "r"
            if (game[0][1] + game[1][1] + game[2][1] == charD[1] * 3): return "b"

            if (game[0][2] + game[1][2] + game[2][2] == charD[0] * 3): return "r"
            if (game[0][2] + game[1][2] + game[2][2] == charD[1] * 3): return "b"

            if (game[0][0] + game[1][1] + game[2][2] == charD[0] * 3): return "r"
            if (game[0][0] + game[1][1] + game[2][2] == charD[1] * 3): return "b"

            if (game[2][0] + game[1][1] + game[0][2] == charD[0] * 3): return "r"
            if (game[2][0] + game[1][1] + game[0][2] == charD[1] * 3): return "b"

        def IsDraw():
            if (str(game[0][0] + game[0][1] + game[0][2] + game[1][0] + game[1][1] + game[1][2] + game[2][0] + game[2][1] + game[2][2]).__contains__("-")):
                return False
            else:
                return True

        def k():
            root.quit()

        def Play():
            if (IsDraw() == False):
                if (game[row][col].__contains__("-")):
                    if (pl[0] == "X"):
                        name.config(text=pl[0], bg='red', fg='white')
                    if (pl[0] == "O"):
                        name.config(text=pl[0], bg='blue', fg='white')
                    game[row][col] = pl[0]
                    # print(game)
                    pl[0], pl[1] = pl[1], pl[0]
                    if (Check() == "r"):
                        k()
                        win = Tk()
                        win.geometry("200x200")
                        win.title("TicTacToe")
                        win.iconbitmap('file-49-512.ico')
                        txt = tkinter.Label(win, text="A piros nyert!")
                        txt.pack()
                        win.mainloop()
                    if (Check() == "b"):
                        k()
                        win = Tk()
                        win.geometry("200x200")
                        win.title("TicTacToe")
                        win.iconbitmap('file-49-512.ico')
                        txt = tkinter.Label(win, text="A kék nyert")
                        txt.pack()
                        win.mainloop()

                    if (IsDraw() == True and Check() != "r" and Check() != "b"):
                        root.quit()
                        win = Tk()
                        win.geometry("200x200")
                        win.title("TicTacToe")
                        txt = tkinter.Label(win, text="Döntetlen!")
                        txt.pack()
                        win.mainloop()

        name = tkinter.Button(root, text=char, width=size, height=int(size / 2), command=Play)
        name.grid(row=row, column=col)


def placeBtn():
    for i in range(3):
        for j in range(3):
            btn = Button(i, j, 25, str(game[i][j]))


placeBtn()

root.mainloop()
