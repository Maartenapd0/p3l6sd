#delen importeren 

from tkinter import *
import time as t
import random as r
import turtle
import random

# voribale de regen boog knop

colors = ["red", "green", "blue"]
colorss = ["orange", "black", "purple"]
color = random.choice(colors)
# venster aanmaken
window = Tk()

window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
#stukje tekst toevoegen
lbl = Label(window, text="your name")
lbl.grid(column=0, row=0)
#tekst kunnen toevoegen
txt = Entry(window,width=10)
txt.grid(column=1, row=2)
#de hele mooie regen boog knop
def regenboog():
    turtle.speed (10)
    turtle.bgcolor ("grey")
    for i in range(15):
        turtle.pensize(3)
        turtle.circle(50)
        turtle.penup()
        turtle.forward(10)
        turtle.right(15)
        turtle.pendown()...
        turtle.color(random.choice(colors))

    turtle.forward(0)

    for i in range(50):
        turtle.pensize(2)
        turtle.circle(50)
        turtle.penup()
        turtle.forward(15)
        turtle.right(6)
        turtle.pendown()
        turtle.color(random.choice(colorss))
    
    for i in range(50):
        turtle.pensize(2)
        turtle.circle(50)
        turtle.penup()
        turtle.forward(20)
        turtle.right(2)
        turtle.pendown()
        turtle.color(random.choice(colorss))
#de submit knop voor je naam
def clicked():
    res = "heey " + txt.get() + " hoe gaat het met jou"
    lbl.configure(text= res)
#de actie voor de knoppen
btn2 = Button(window, text="rainbow", command=regenboog)
btn2.grid(column=0, row=2)
btn1 = Button(window, text="Click Me", command=clicked)
btn1.grid(column=2, row=0)
# de hooft loop waar door alles blijft uitvoeren.
window.mainloop()