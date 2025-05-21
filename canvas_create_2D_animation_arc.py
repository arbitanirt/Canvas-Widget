import tkinter as tk
from tkinter import *
import time


mainwindow =tk.Tk()
mainwindow.title("Canvas for drawing")

can = Canvas(mainwindow,bg='yellow', relief='raised', bd=2, height=400, width=400  )

#def start_btn_handler():
#    arc = can.create_arc(10, 10, 380, 380, extent=359, fill='blue')
#    mainwindow.update_idletasks()
#    time.sleep(0.5)
#    can.delete(arc)

list_color = ['red', 'green', 'blue']

def start_btn_handler():
    for j in range(3):
        for i in range(360):
            arc = can.create_arc(10, 10, 380, 380, extent=i, fill=list_color[j])
            mainwindow.update_idletasks()
            time.sleep(0.001)
            can.delete(arc)

start_btn = Button(mainwindow, text="START", command=start_btn_handler)
start_btn.pack()

can.pack()


mainwindow.config(pady=10)
mainwindow.geometry('500x500')
mainwindow.mainloop()