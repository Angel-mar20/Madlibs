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

    