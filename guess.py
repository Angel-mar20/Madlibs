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

win.mainloop()