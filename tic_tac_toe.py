from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Team 10 - Tic-Tac-Toe')

# root.iconbitmap('favicon.ico')

# X starts so True
clicked = "X"
count = 0
playerTurn = True

# Button clicked Functions
# k = random.randint(1, 9)

def b_click(b):
  global clicked, count, playerTurn
  if b["text"] == " ":
    b["text"] = clicked
    if clicked == "X":
      clicked = "O"
    else:
      clicked = "X"
    count += 1
    checkifwon()
  else:
    messagebox.showerror(
      "Tic Tac Toe", "Hey! That box has been selected\nPick another one")
  playerTurn = False if playerTurn else False


def start_game():
  if not playerTurn:
    pass

# Reset Buttons
def reset():
  b1["text"] = " "
  b2["text"] = " "
  b3["text"] = " "
  b4["text"] = " "
  b5["text"] = " "
  b6["text"] = " "
  b7["text"] = " "
  b8["text"] = " "
  b9["text"] = " "
  b1.config(bg="white")
  b2.config(bg="white")
  b3.config(bg="white")
  b4.config(bg="white")
  b5.config(bg="white")
  b6.config(bg="white")
  b7.config(bg="white")
  b8.config(bg="white")
  b9.config(bg="white")
  set_button_state(NORMAL)
  global clicked, count
  clicked = "X"
  count = 0

#Functions
def set_button_state(bState):
  b1.config(state=bState)
  b2.config(state=bState)
  b3.config(state=bState)
  b4.config(state=bState)
  b5.config(state=bState)
  b6.config(state=bState)
  b7.config(state=bState)
  b8.config(state=bState)
  b9.config(state=bState)

def turnblue(s1, s2, s3):
  s1.config(bg="blue")
  s2.config(bg="blue")
  s3.config(bg="blue")

def winMessage(sym):
  winMsg = sym + " Wins!, Play Again?" 
  if messagebox.askquestion("Tic Tac Toe", winMsg) == "yes":
    reset() 
  else:
    set_button_state(DISABLED)

# Check for player win
def checkifwon():
  global winner, count
  winner = False

  #Check if X wins
  if b1["text"] != " " and b1["text"] == b2["text"] and b1["text"] == b3[
            "text"]:
    turnblue(b1, b2, b3)
    winner = True
    winMessage(b1["text"])

  elif b4["text"] != " " and b4["text"] == b5["text"] and b4["text"] == b6[
            "text"]:
    turnblue(b4, b5, b6)
    winner = True
    winMessage(b4["text"])

  elif b7["text"] != " " and b7["text"] == b8["text"] and b7["text"] == b9[
            "text"]:
    turnblue(b7, b8, b9)
    winner = True
    winMessage(b7["text"])

  elif b1["text"] != " " and b1["text"] == b4["text"] and b1["text"] == b7[
            "text"]:
    turnblue(b1, b4, b7)
    winner = True
    winMessage(b1["text"])

  elif b2["text"] != " " and b2["text"] == b5["text"] and b2["text"] == b8[
            "text"]:
    turnblue(b2, b5, b8)
    winner = True
    winMessage(b2["text"])

  elif b3["text"] != " " and b3["text"] == b6["text"] and b3["text"] == b9[
            "text"]:
    turnblue(b3, b6, b9)
    winner = True
    winMessage(b3["text"])

  elif b1["text"] != " " and b1["text"] == b5["text"] and b1["text"] == b9[
            "text"]:
    turnblue(b1, b5, b9)
    winner = True
    winMessage(b1["text"])

  elif b3["text"] != " " and b3["text"] == b5["text"] and b3["text"] == b7[
            "text"]:
    turnblue(b3, b5, b7)
    winner = True
    winMessage(b3["text"])

  if count == 9 and winner == False:
        if messagebox.askquestion("Tic Tac Toe", "It's a tie! No One Wins!\nPlay Again?") == "yes":
          reset() 
        else:
          set_button_state(DISABLED)

                       #Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

b1 = Button(root, 
              text=" ",
              font= ("Helvetica", 20),
              height=3,
              width=6,
              bg="white",
              command=lambda: b_click(b1))
b2 = Button(root,
              text=" ",
              font=("Helvetica", 20),
              height=3,
              width=6,
              bg="white",
              command=lambda: b_click(b2))
b3 = Button(root,
                text=" ",
                font=("Helvetica", 20),
                height=3,
                width=6,
                bg="white",
                command=lambda: b_click(b3))
b4 = Button(root,
                text=" ",
                font=("Helvetica", 20),
                height=3,
                width=6,
                bg="white",
                command=lambda: b_click(b4))
b5 = Button(root,
              text=" ",
              font=("Helvetica", 20),
              height=3,
              width=6,
              bg="white",
              command=lambda: b_click(b5))
b6 = Button(root,
              text=" ",
              font=("Helvetica", 20),
              height=3,
              width=6,
              bg="white",
              command=lambda: b_click(b6))

b7 = Button(root,
              text=" ",
              font=("Helvetica", 20),
              height=3,
              width=6,
              bg="white",
              command=lambda: b_click(b7))

b8 = Button(root,
              text=" ",
              font=("Helvetica", 20),
              height=3,
              width=6,
              bg="white",
              command=lambda: b_click(b8))

b9 = Button(root,
              text=" ",
              font=("Helvetica", 20),
              height=3,
              width=6,
              bg="white",
              command=lambda: b_click(b9))

    #Grid for buttons on screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

reset()
root.mainloop()
