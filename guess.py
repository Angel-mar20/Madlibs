import random
from tkinter import Tk

win = Tk()
win.title("guess game")
win.geometry('750x750')
win.config(bg="light blue")

hint = StringVar()
score = IntVar()
final_score= IntVar()
guess= IntVar()

win.mainloop()