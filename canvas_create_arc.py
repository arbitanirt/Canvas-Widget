import tkinter as tk
from tkinter import *


mainwindow =tk.Tk()
mainwindow.title("Canvas for drawing")

can = Canvas(mainwindow,bg='yellow', relief='raised', bd=2, height=400, width=400  )

#can.create_arc(10,10, 200, 200, extent=270)
arc = can.create_arc(10,10, 300, 300, extent=359, fill='blue')
print('Arc : ', arc)

line = can.create_line(200, 10, 200, 300, fill='red')
print('Line : ', line)

can.delete(line)

can.pack()



mainwindow.geometry('500x500')
mainwindow.mainloop()