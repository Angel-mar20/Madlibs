#Import the necessary modules
import random
from tkinter import messagebox
from tkinter import *

def generate_password():
    try:
       repeat = int(repeat_entry.get())
       length = int(length_entry.get())