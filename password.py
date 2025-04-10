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