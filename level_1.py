# Tic Tac Toe game with GUI by using tkinter.
import random
from tkinter import *  # it imports all the functions and built-in modules in the tkinter library.
import pygame  # It is used to develop 2-D games and is a platform where we can set python modules to develop a game.
from functools import \
    partial  # Partial functions allow us to fix a certain number of arguments of a function and generate a new function.
from tkinter import messagebox  # To display a message through messagebox
import copy  # It is used to create deepycopy for copying set of elements .
from PIL import ImageTk, Image  # To insert the image by using these functions

sign = 0  # sign variable to decide the turn of which player

global board
board = [[" " for x in range(3)] for y in range(3)]  # Creates an empty grid board


# Checking the winner marker in noughts and crosses  (X/O) , according to the rules of the game
def winner(b, marker):
    return ((b[0][0] == marker and b[0][1] == marker and b[0][2] == marker) or  # Horizontal checking
            (b[1][0] == marker and b[1][1] == marker and b[1][2] == marker) or
            (b[2][0] == marker and b[2][1] == marker and b[2][2] == marker) or
            (b[0][0] == marker and b[1][0] == marker and b[2][0] == marker) or  # Vertical checking
            (b[0][1] == marker and b[1][1] == marker and b[2][1] == marker) or
            (b[0][2] == marker and b[1][2] == marker and b[2][2] == marker) or
            (b[0][0] == marker and b[1][1] == marker and b[2][2] == marker) or  # diagnol Checking
            (b[0][2] == marker and b[1][1] == marker and b[2][0] == marker))


# Configure text on button while playing with another player
def get_text(i, j, gb, marker1, marker2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            marker1.config(state=DISABLED)
            marker2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            marker2.config(state=DISABLED)
            marker1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        messagebox.showinfo("Winner", "Player 1 won the match")
    elif winner(board, "O"):
        gb.destroy()
        messagebox.showinfo("Winner", "Player 2 won the match")
    elif (isfull()):
        gb.destroy()
        messagebox.showinfo("Tie Game", "Tie Game")


# Checking the gameboard if the player can push the button or not
def isfree(i, j):
    return board[i][j] == " "


# Checking the grid board is full or not
def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0):
            flag = False
    return flag


# Creating the GUI of game board for Player vs player
def gameboard_player(game_board, mark1, mark2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, mark1, mark2)
            button[i][j] = Button(game_board, bd=7, command=get_t, height=7, width=14, relief="raised", bg="#ffccb3")
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Deciding the next move of system according to the humans move
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
                boardcopy = copy.deepcopy(board)  # a copy of board is copied in other object called board
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]


# Configuring the text on button while playing with system
def get_text_pc(i, j, gb, marker1, marker2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            marker1.config(state=DISABLED)
            marker2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            marker2.config(state=DISABLED)
            marker1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")  # message box for X player wins
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
            get_text_pc(move[0], move[1], gb, marker1, marker2)


# Creating the GUI of game board for play along with system
def gameboard_pc(game_board, marker1, marker2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, marker1, marker2)
            button[i][j] = Button(game_board, bd=7, command=get_t, height=7, width=14, relief="raised", bg="#CC9966")
            button[i][j].grid(row=m, column=n)

    game_board.mainloop()


# Initializing the game board to play with system
def with_computer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    game_board.resizable(False, False)
    game_board.iconbitmap("C:/Users/KATTAKART/Downloads/favicon.ico")
    marker1 = Button(game_board, text="Player : X", width=8, font=('bold', 10), fg='black', bg="tan", state=DISABLED)
    marker1.grid(row=1, column=1)
    marker2 = Button(game_board, text="Computer : O", width=9, font=('bold', 10), fg='black', bg="tan", state=DISABLED)
    marker2.grid(row=2, column=1)
    gameboard_pc(game_board, marker1, marker2)


# Initialize the game board to play with another player
def with_player(game_board):
    game_board.destroy()  # If we want to clear the frame content or delete all the widgets inside the frame we use this destroy function()
    game_board = Tk()  # Displays the game window interface
    game_board.title("Tic Tac Toe")
    game_board.resizable(False, False)  # Disabling the resize of the gridboard
    game_board.iconbitmap("C:\\Users\\KATTAKART\\Downloads\\favicon.ico")
    marker1 = Button(game_board, text="Player 1 : X", width=10, state=DISABLED)
    marker1.grid(row=1, column=1)
    marker2 = Button(game_board, text="Player 2 : O", width=10, state=DISABLED)
    marker2.grid(row=2, column=1)
    gameboard_player(game_board, marker1, marker2)


# main function
def play():
    menu = Tk()
    menu.geometry("418x500")
    menu.title("Tic Tac Toe")
    menu.iconbitmap("C:/Users/KATTAKART/Downloads/favicon.ico")
    menu.resizable(False, False)
    menu.img = Image.open("C:\\Users\\KATTAKART\\Downloads\\Temp-500x500.jpg")  # Setting up the background image
    menu.bg = ImageTk.PhotoImage(menu.img)
    welcome_frame = Label(menu, image=menu.bg)
    welcome_frame.pack(fill=BOTH, expand=True)
    pygame.mixer.init()
    with_pc = partial(with_computer, menu)
    with_hum = partial(with_player, menu)

    Label(welcome_frame, text="--Choose the player mode--", bg='light yellow', fg='black',
          font=('', 20, 'bold')).pack(padx=10, pady=40, side='top')
    singleimg = PhotoImage(file=r"C:\Users\KATTAKART\Pictures\single player.png")
    Button(welcome_frame, text="Single Player", command=with_pc,image=singleimg,
           bg='tan', fg='black',
           font=('', 18, 'italic'),
           ).pack(padx=12, pady=12, side='left')
    doubleimg = PhotoImage(file=r"C:\Users\KATTAKART\Downloads\multiplayer.png")
    Button(welcome_frame, text="Multi Player", command=with_hum, bg='tan', fg='black',image=doubleimg,
           font=('', 18, 'italic'),
           ).pack(padx=12, pady=12, side='right')

    # Defining the toggle button used to turn off and on the music at a time.
    def Simpletoggle():
        if toggle_button.config('text')[-1] == '🔊':
            toggle_button.config(text='🔇')
            pygame.mixer.music.stop()
        else:
            toggle_button.config(text='🔊', command=play_sound())

    toggle_button = Button(welcome_frame, text="🔇", bg="papaya whip", width=3, font=("", 20), command=Simpletoggle)
    toggle_button.pack(pady=30,side='bottom')

    def play_sound():  # Defining the function to play music.
        pygame.mixer.music.load("C:/Users/KATTAKART/Downloads/Happy-Whistling-Ukulele.mp3")  # Loading the music
        pygame.mixer.music.play()

    menu.mainloop()  # execute when we want to run our application
