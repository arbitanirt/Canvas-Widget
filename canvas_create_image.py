import tkinter as tk
from tkinter import *


mainwindow =tk.Tk()
mainwindow.title("Canvas for drawing")

can = Canvas(mainwindow,bg='yellow', relief='raised', bd=2, height=400, width=400  )
img = PhotoImage(file='logo.png')

can.create_image(100, 100, image=img)



can.pack()






mainwindow.geometry('500x500')
mainwindow.mainloop()