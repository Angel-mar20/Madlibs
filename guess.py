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

win.mainloop()