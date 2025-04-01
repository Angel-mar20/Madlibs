from tkinter import *
def Sample1(win):
    def sinal(t1: Toplevel, name, age, music, drinks, food):

        Text = f'''
           my name is {name}, i have {age} years old my favourite music is {music}
           when i'm listerning music i prefer to use {drinks} and some bytes and my 
           and my favourite food is {food}'''
        
        t1.geometry(newGeometry=('500x500'))
        Label(t1, text=('Story:'), wraplength=t1.winfo_width()).place(x=160,y=310)
        Label(t1, text=Text, wraplength=t1.winfo_width()).place(x=0,y=330) 
    Newscreen = Toplevel(win, bg="pink")
    Newscreen.title("Simple story")
    Newscreen.geometry('500x500')
    Label(Newscreen, text=('Simple Intro')).place(x=150, y=0)
    Label(Newscreen, text=('Name:')).place(x=0,y=35)
    Label(Newscreen, text=('Age:')).place(x=0,y=70)
    Label(Newscreen, text=('Music:')).place(x=0,y=110)
    Label(Newscreen, text=('Drink:')).place(x=0,y=150)
    Label(Newscreen, text=('Food:')).place(x=0,y=190)

    name = Entry(Newscreen, width=20)
    name.place(x=270,y=35)
    age = Entry(Newscreen, width=20)
    age.place(x=270,y=70)
    music = Entry(Newscreen, width=20)
    music.place(x=270,y=110)
    drink = Entry(Newscreen, width=20)
    drink.place(x=270,y=150)
    food = Entry(Newscreen, width=20)
    food.place(x=270,y=190)

    