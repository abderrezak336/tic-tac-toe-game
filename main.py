from tkinter import *
from tkinter import messagebox


window = Tk()

window.title("Tic-Tac-Toe Gui Game")
window.config(width=600, height=600, background="black")

canvas = Canvas(height=200, width=600, background='black', highlightthickness=0, borderwidth=0)

score_text = canvas.create_text(300, 100, text="X:    VS    O:", fill='white', font=("Calibri", 60, "bold"))

canvas.grid(row=1, column=3)

empty_img = PhotoImage(file="Assets/empty.png")
x_img = PhotoImage(file="Assets/x.png")
o_img = PhotoImage(file="Assets/o.png")
green_o = PhotoImage(file="Assets/green_o.png")
green_x = PhotoImage(file="Assets/green_x.png")


is_my_turn = 0
btn_list = []

#create the board list the 0 and 1 represent nothing you can write anything
board = [[0, 1, 1],
         [1, 0, 0],
         [0, 0, 1]]

is_winner = False
x, o = 0, 0


def list_type(my_list):
    list_type = True
    for l in my_list:
        if type(l) is int:
            list_type = False
    return list_type


def reset_board():
    global board
    board = [[0, 1, 1],
             [1, 0, 0],
             [0, 0, 1]]
    for item in range(9):
        btn_list[item].config(image=empty_img)
        btn_list[item]["state"] = "normal"

#reset the board and increase players score
def clean_board(p):
    global x, o
    if p == "x":
        x += 1
        reset_board()

    elif p == "o":
        o += 1
        reset_board()

    canvas.itemconfig(score_text, text=f"X: {x}    VS    O: {o}")



#change the color of board into green
def update_board(vh, line, var):
    if vh == "h":
        if line == 0:
            btn_list[0].config(image=var)
            btn_list[3].config(image=var)
            btn_list[6].config(image=var)
        elif line == 1:
            btn_list[1].config(image=var)
            btn_list[4].config(image=var)
            btn_list[7].config(image=var)
        elif line == 2:
            btn_list[2].config(image=var)
            btn_list[5].config(image=var)
            btn_list[8].config(image=var)

    elif vh == "v":
        if line == 0:
            btn_list[0].config(image=var)
            btn_list[1].config(image=var)
            btn_list[2].config(image=var)
        elif line == 1:
            btn_list[3].config(image=var)
            btn_list[4].config(image=var)
            btn_list[5].config(image=var)
        elif line == 2:
            btn_list[6].config(image=var)
            btn_list[7].config(image=var)
            btn_list[8].config(image=var)
    else:
        if line == "r":
            btn_list[0].config(image=var)
            btn_list[4].config(image=var)
            btn_list[8].config(image=var)
        elif line == "l":
            btn_list[2].config(image=var)
            btn_list[4].config(image=var)
            btn_list[6].config(image=var)


#ask the user if he want to play again
def ask_user(p):
    msg_q = messagebox.askquestion(title=f"The Winner is {p.upper()}", message=f"The Winner is {p.upper()}"
                                                                               f" Do You Want To Play Again ?: ".lower())
    if msg_q == 'yes':
        clean_board(p)
    else:
        window.quit()



def check_line(lst, line, vh):
    global is_winner
    if len(set(lst)) == 1:
        is_winner = True
        if lst[0] == "x":
            update_board(vh, line, green_x)
            ask_user(lst[0])
        elif lst[0] == "o":
            update_board(vh, line, green_o)
            ask_user(lst[0])






def check_winner():
    global board, is_winner
    v = 0
    #check vertical
    for l in board:
        check_line(l, v, "v")
        v += 1

    #check horizantel
    horizantel_lst = []
    h = 0
    for i in range(3):
        for j in range(3):
            horizantel_lst.append(board[j][i])

        check_line(horizantel_lst, h, "h")
        h += 1
        horizantel_lst = []

    #check triangular
    if (board[0][0] == board[1][1] == board[2][2]):
        is_winner = True
        if board[0][0] == "x":
            update_board("t", "r", green_x)
            ask_user(board[0][0])
        elif board[0][0] == "o":
            update_board("t", "r", green_o)
            ask_user(board[0][0])




    if (board[0][2] == board[1][1] == board[2][0]):
        is_winner = True
        if board[0][2] == "x":
            update_board("t", "l", green_x)
            ask_user(board[0][2])
        elif board[0][2] == "o":
            update_board("t", "l", green_o)
            ask_user(board[0][2])



    #check if there is no winner
    if list_type(board[0]) and list_type(board[1]) and list_type(board[2]):
        messagebox.showinfo(title="No Winner", message="Game is drewn")
        reset_board()



#check which buttons pressed and disabled the button
def check_state(image_var, btn_index, t, j):
    global is_my_turn, board
    btn_list[btn_index].config(image=x_img if image_var == "x" else o_img)
    btn_list[btn_index]["state"] = "disabled"
    board[t][j] = image_var
    is_my_turn += 1
    check_winner()



#write x or o on borad
def write(i, t, j):
    global is_my_turn
    if(is_my_turn % 2 == 0):
        check_state("x", i, t, j)
    else:
        check_state("o", i, t, j)



#create the board
count = 0
for i in range(3):
    for j in range(3):
        button = Button(image=empty_img, highlightthickness=0, borderwidth=0, command=lambda k=(count, i, j): write(k[0], k[1], k[2]))
        button.grid(row=i, column=j)
        btn_list.append(button)
        count += 1

window.mainloop()