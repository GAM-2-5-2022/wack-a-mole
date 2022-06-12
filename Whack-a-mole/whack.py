from tkinter import *
import random
import time

x = 0

top = Tk()

top.geometry("2000x1000")

top.title("Whack-a-mole")
c = Canvas(top, bg = "lime", height = "1100", width = "2000")
c.place(x=0, y=0)

photo = PhotoImage(file = r"mole.png")
photo2 = PhotoImage(file = r"play.png")

def start():
    global b
    global a
    a.destroy()
    b = Button(top,image=photo, command=click, bd=0, bg="lime")
    b.place(x=random.randint(0, 1800), y=random.randint(100, 800))
    top.after(60000, gameover)

a = Button(top, command=start, bg="lime", bd=0, image=photo2)
a.place(x=850, y=450)
     
def click():
    global x
    global b
    b.destroy()
    x+=1
    text_label = "score: " + str(x)
    Label(top, text = text_label,font=("bold", 40), bg="lime", bd=0).place(x=850, y=2) 
    b = Button(top,image=photo, command=click, bd=0, bg="lime")
    b.place(x=random.randint(0, 1700), y=random.randint(100, 700))

def gameover():
    global x
    newWindow = Toplevel(top)
    newWindow.title("Gameover")
    newWindow.geometry("300x100")
    c = Canvas(newWindow, bg = "lime", height = "1100", width = "2000")
    c.place(x=0, y=0)
    text_label = "score: " + str(x)
    Label(newWindow, text = text_label,font=("bold", 40), bg="lime", bd=0).pack()
    top.withdraw()

top.mainloop()
