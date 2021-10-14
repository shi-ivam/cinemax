import random
from tkinter import *
from tkinter import ttk
from tkinter import font
root = Tk()
root.geometry("800x400")
frm = Frame(root)



heading = Label(frm,text="Cinemax",font=("Helvetica",25))
l1 = Label(frm,text="First Name : ")
l2 = Label(frm,text="Last Name : ")
e1 = Entry(frm,background="lightgrey")
e2 = Entry(frm,background="lightgrey")

heading.grid(row=1,column=1,columnspan=2)

l1.grid(row=2,column=1)
l2.grid(row=3,column=1)
e1.grid(row=2,column=2)
e2.grid(row=3,column=2)

frm.grid(row=1,column=1)
frm.pack(expand=True)

frm.mainloop()