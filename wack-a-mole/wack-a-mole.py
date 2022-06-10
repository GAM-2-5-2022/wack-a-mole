from tkinter import *
from tkinter.ttk import *
import random
import time

lives = 3
x = 0
top = Tk()

top.geometry("900x1000")

c = Canvas(top, bg = "green", height = "9000", width = "10000")
c.place(x=0, y=0)

photo = PhotoImage(file = r"mole.png")
def click():
    global photo
    global b
    b.destroy()
    time.sleep(0.2)
    b = Button(top,image=photo, command=click)
    b.place(x=random.randint(100, 800), y=random.randint(200, 800))
    
def btn():
    global b
    b = Button(top,image=photo, command=click)
    b.place(x=random.randint(100, 800), y=random.randint(200, 800))

btn()

top.mainloop()

