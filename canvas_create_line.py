import tkinter as tk
from tkinter import *


mainwindow =tk.Tk()
mainwindow.title("Canvas for drawing")

can = Canvas(mainwindow,bg='yellow', relief='raised', bd=2, height=400, width=400  )

can.create_line(10, 200, 380, 200)
can.create_line(200, 10, 200, 380)


can.pack()






mainwindow.geometry('500x500')
mainwindow.mainloop()