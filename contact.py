from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x500')
root.title("Contact sample")
root.config(bg="#f0fffc")
root.resizable(0,0)

contactlist = [
    ['Rahma Ramadhan', '0765323412'],
    ['Karem Kareem', '0743219078']
    ['Siddharth Nigam','07369854712'],
    ['Gaurav Patil', '07521155222'],
    ['Abhishek Nikam', '0678945614'],
    ['Sakshi Gaikwad', '0758745246'],
    ['Mohit Paul', '075846975'],
    ['Karan Patel', '095647892'],
    ['Sam Sharma', '0689685320'],
    ['John Maheshwari', '0798564785'],
    ['Ganesh Pawar','0685967412']
]

name = StringVar()
contact = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman'), bg='#d3f3f5', width=20, height=20, borderwidth=3, relief='groove')
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)



root.mainloop()
