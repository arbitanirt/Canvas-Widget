import tkinter as tk
from tkinter import *


mainwindow =tk.Tk()
mainwindow.title("Canvas for drawing")

can = Canvas(mainwindow,bg='yellow', relief='raised', bd=2, height=400, width=400  )

can.create_oval(10, 10, 100, 100)
can.create_oval(10, 10, 380, 380)
can.create_oval(280, 10, 380, 100)
can.create_oval(150, 150, 250, 250)

can.pack()






mainwindow.geometry('500x500')
mainwindow.mainloop()