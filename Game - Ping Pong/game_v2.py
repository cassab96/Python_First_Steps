# Ping-Pong Game
# By cassabr

# Imports
from tkinter import *
import random
import time

# Variable receive the value by the player
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))

# Variable 
length = 500/level

# Instance of Object Tk
root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# Variable receive the function Canvas result
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()
root.update()

# Variables
count = 0
lost = False

# Class 'Bola'
class Bola:
    def __init__(self, canvas, Barra, color):

        # Variables
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        # List
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        # Variables
        self.x = starts_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # Function
    def draw(self):

        # Variables
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        # If Conditional
        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        # Variable
        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # If Conditional nested
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1

                # Call function
                score()

        # If Conditional
        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
            
        else:
            # Call function
            game_over()

            # Variables
            global lost
            lost = True

# Class 'Barra'
class Barra:
    def __init__(self, canvas, color):

        # Variables
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    # Function
    def draw(self):

        # Call Method
        self.canvas.move(self.id, self.x, 0)

        # Variable
        self.pos = self.canvas.coords(self.id)

        # If Conditional
        if self.pos[0] <= 0:
            self.x = 0

        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    # Function
    def move_left(self, event):

        # If Conditional
        if self.pos[0] >= 0:
            self.x = -3

    # Function
    def move_right(self, event):

        # If Conditional
        if self.pos[2] <= self.canvas_width:
            self.x = 3

# Function
def start_game(event):

    # Variables
    global lost, count
    lost = False
    count = 0

    # Call function
    score()

    # Variable receive function result
    canvas.itemconfig(game, text=" ")

    # Objects Methods
    time.sleep(1)
    Barra.draw()
    Bola.draw()

# Function
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

# Function
def game_over():
    canvas.itemconfig(game, text="Game over!")

# Objects Instances 'Barra' and 'Bola'
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

# Variables receive functions results
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))
canvas.bind_all("<Button-1>", start_game)

# Execute the program 
root.mainloop()




