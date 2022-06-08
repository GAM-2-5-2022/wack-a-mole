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


def click():
    time.sleep(1)
    b.pack_forget()
while x<2:
    time.sleep(1)
    b = Button(top, command=click)
    b.place(x=random.randint(100, 800), y=random.randint(200, 800))
    x +=1
print(x)


top.mainloop()


