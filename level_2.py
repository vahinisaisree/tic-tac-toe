""" tic tac toe game 5X5 level medium"""

# importing all necessary libraries
import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
import pygame
from PIL import ImageTk, Image

# sign variable to decide the turn of which player
sign = 0

# Creates an empty board
global board
board = [[" " for x in range(5)] for y in range(5)]

# 28 winning chances
# according to the rules of the game
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l and b[0][3] == l and b[0][4] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l and b[1][3] == l and b[1][4] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l and b[2][3] == l and b[2][4] == l) or
            (b[3][0] == l and b[3][1] == l and b[3][2] == l and b[3][3] == l and b[3][4] == l) or
            (b[4][0] == l and b[4][1] == l and b[4][2] == l and b[4][3] == l and b[4][4] == l) or  # over row checking

            (b[0][0] == l and b[1][0] == l and b[2][0] == l and b[3][0] == l and b[4][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l and b[3][1] == l and b[4][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l and b[3][2] == l and b[4][2] == l) or
            (b[0][3] == l and b[1][3] == l and b[2][3] == l and b[3][3] == l and b[4][3] == l) or
            (b[0][4] == l and b[1][4] == l and b[2][4] == l and b[3][4] == l and b[4][4] == l) or  # column checking

            (b[0][0] == l and b[1][1] == l and b[2][2] == l and b[3][3] == l and b[4][4] == l) or
            (b[0][4] == l and b[1][3] == l and b[2][2] == l and b[3][1] == l and b[4][0] == l))   # diagnose checking


# Configure text on button while playing with another player
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match")
    elif (isfull()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")


# Check if the player can push the button or not
def isfree(i, j):
    return board[i][j] == " "


# Check the board is full or not
def isfull():
    flag = True
    for i in board:
        if i.count(' ') > 0:
            flag = False
    return flag


# Create the GUI of game board for play along with another player
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(5):
        m = 5 + i
        button.append(i)
        button[i] = []
        for j in range(5):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8,bg="#CC9966")
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Decide the next move of system
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = [] # placing computer move at corners first and in the center by using index value
        for i in possiblemove:
            if i in [[0, 0], [0, 4], [4, 0], [4, 4], [2, 2], [1, 1], [1, 3], [3, 1], [3, 3]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []  # placing the computer move at edges and inner edges too
        for i in possiblemove:
            if i in [[0, 2], [2, 0], [2, 4], [4, 2], [1, 2], [2, 1], [3, 2], [2, 3]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]
        remain = []  # placing the computer move at the remaining places according to the player move
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [0, 3], [1, 4], [3, 0], [4, 1], [4, 3], [3, 4]]:
                remain.append(i)
        if len(remain) > 0:
            move = random.randint(0, len(remain) - 1)
            return remain[move]


# displaying messages by using message box like who won the match and tie
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)  # player 1 is disabled when the another player is active
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif (isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if (x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)


# game board for single player and pc
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(5):
        m = 5 + i
        button.append(i)
        button[i] = []
        for j in range(5):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8,bg="#CC9966")
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# telling whose turn is this in single player
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    game_board.iconbitmap("C:\\Users\\KATTAKART\\Downloads\\favicon.ico")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=2)
    l2 = Button(game_board, text="Computer : O", width=10, state=DISABLED)
    l2.grid(row=2, column=2)
    gameboard_pc(game_board, l1, l2)


# telling whose turn is this in multiplayer
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    game_board.iconbitmap("C:\\Users\\KATTAKART\\Downloads\\favicon.ico")
    l1 = Button(game_board, text="Player 1 : X", width=10)
    l1.grid(row=1, column=2)
    l2 = Button(game_board, text="Player 2 : O", width=10, state=DISABLED)
    l2.grid(row=2, column=2)
    gameboard_pl(game_board, l1, l2)


# main function
def play1():
    menu = Tk()
    menu.geometry("418x500")
    menu.title("Tic Tac Toe")
    menu.iconbitmap("C:/Users/KATTAKART/Downloads/favicon.ico")
    menu.resizable(False,False)
    menu.img = Image.open("C:\\Users\\KATTAKART\\Downloads\\Temp-500x500.jpg")  # Setting up the background image
    menu.bg = ImageTk.PhotoImage(menu.img)
    welcome_frame = Label(menu, image=menu.bg)
    welcome_frame.pack(fill=BOTH, expand=True)
    pc = partial(withpc, menu)
    player = partial(withplayer, menu)

    Button(welcome_frame, text="--select player mode--", bg='light yellow', fg='black',
           font=('', 20, 'bold')).pack(padx=10, pady=20, side='top')

    singleimg= PhotoImage(file=r"C:\Users\KATTAKART\Pictures\single player.png")
    Button(welcome_frame, image=singleimg, command=pc).pack(padx=30, pady=5, side='left')

    doubleimg = PhotoImage(file=r"C:\Users\KATTAKART\Downloads\multiplayer.png")
    Button(welcome_frame, text="multi player", command=player,image=doubleimg,bg='tan').pack(padx=30, pady=5, side='right')

    def Simpletoggle():
        if toggle_button.config('text')[-1] == '🔊':
            toggle_button.config(text='🔇')
            pygame.mixer.music.stop()
        else:
            toggle_button.config(text='🔊', command=play_sound())

    toggle_button = Button(welcome_frame, text="🔇", bg="papaya whip", width=3, font=("", 20), command=Simpletoggle)
    toggle_button.pack(side='bottom',pady=20)

    def play_sound():  # Defining the function to play music.
        pygame.mixer.music.load("C:/Users/KATTAKART/Downloads/Happy-Whistling-Ukulele.mp3")  # Loading the music
        pygame.mixer.music.play()

    menu.mainloop()


