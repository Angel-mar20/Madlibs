import tkinter as tk
from tkinter import *
import random



win = tk.Tk()
win.title("guess game")
win.geometry('750x750')
win.config(bg="light blue")
num=random.randint(1,50)

hint = StringVar()
score = IntVar()
final_score= IntVar()
guess= IntVar()

hint.set("Guess a number between 1 to 50 ")
score.set(5)
final_score.set(score.get())

def fun():
    x=guess.get()
    final_score.set(score.get())
    if score.get()>0:
        if x > 20 or x<0:
            hint.set("You just lost 1 Chance")
            score.set(score.get()-1)
            final_score.set(score.get())
    
        elif num==x:
            hint.set("Congratulation YOU WON!!!")
            score.set(score.get()-1)
            final_score.set(score.get())
      
        elif num > x:
            hint.set("Your guess was too low: Guess a number higher ")
            score.set(score.get()-1)
            final_score.set(score.get())
        elif num < x:
            hint.set("Your guess was too High: Guess a number Lower ")
            score.set(score.get()-1)
            final_score.set(score.get())
    else:
         hint.set("Game Over You Lost")

win.mainloop()