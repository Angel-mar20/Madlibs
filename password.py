#Import the necessary modules
import random
from tkinter import messagebox
from tkinter import *

def generate_password():
    try:
       repeat = int(repeat_entry.get())
       length = int(length_entry.get())
    except:
       messagebox.showerror(message="Please key in the required inputs")
       return 

    if repeat == 1:
       password = random.sample(character_string,length) 

    else:
       password = random.choices(character_string,k=length) 

    password=''.join(password)
    password_v = StringVar()
    password="Created password: "+str(password)