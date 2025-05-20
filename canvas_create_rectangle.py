import tkinter as tk
from tkinter import *


mainwindow =tk.Tk()
mainwindow.title("Canvas for drawing")

can = Canvas(mainwindow,bg='yellow', relief='raised', bd=2, height=400, width=400  )

can.create_rectangle(10, 10, 100, 100, fill="blue", width="10")

can.create_rectangle(300, 300, 400, 400, fill="green", width="5")

can.create_rectangle(320, 320, 380, 380, fill="black", width="2")




can.pack()






mainwindow.geometry('500x500')
mainwindow.mainloop()