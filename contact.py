from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x550')
root.config(bg = '#d3f3f5')
root.title('PythonGeeks Contact Book')
root.resizable(0,0)
contactlist = [
    ['Siddharth Nigam','369854712'],
    ['Gaurav Patil', '521155222'],
    ['Abhishek Nikam', '78945614'],
    ['Sakshi Gaikwad', '58745246'],
    ['Mohit Paul', '5846975'],
    ['Karan Patel', '5647892'],
    ['Sam Sharma', '89685320'],
    ['John Maheshwari', '98564785'],
    ['Ganesh Pawar','85967412']
    ]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)
root.mainloop()