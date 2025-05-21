import tkinter as tk
from tkinter import *
import time


mainwindow =tk.Tk()
mainwindow.title("Canvas for drawing")

can = Canvas(mainwindow,bg='yellow', relief='raised', bd=2, height=400, width=400  )

circle_id = can.create_oval(10, 10, 50, 50, fill='blue')


def start_btn_handler():
    for i in range(50):
        can.move(circle_id, 5, 5)
        mainwindow.update_idletasks()
        time.sleep(0.1)

    for i in range(50):
        can.move(circle_id, -5, -5)
        mainwindow.update_idletasks()
        time.sleep(0.1)

start_btn = Button(mainwindow, text="START", command=start_btn_handler)
start_btn.pack()


can.pack()


mainwindow.config(pady=10)
mainwindow.geometry('500x500')
mainwindow.mainloop()