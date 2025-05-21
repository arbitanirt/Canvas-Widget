import tkinter as tk
from tkinter import *


mainwindow =tk.Tk()
mainwindow.title("Canvas for drawing")

can = Canvas(mainwindow,bg='yellow', relief='raised', bd=2, height=400, width=400  )

points = [10, 200, 200, 10, 390, 200, 200, 390]
can.create_polygon(points, fill ='blue', outline='red')

points = [20, 180, 180, 20, 370, 180, 180, 370]
can.create_polygon(points, fill ='green', outline='red')

can.pack()



mainwindow.geometry('500x500')
mainwindow.mainloop()