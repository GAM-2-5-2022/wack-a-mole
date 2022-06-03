from tkinter import *
from tkinter.ttk import *
import random
import time

lives = 3
score = 0

top = Tk()

top.geometry("900x1000")

c = Canvas(top, bg = "green", height = "900", width = "1000")

c.pack()

b = Button(top,text = "Simple") 
photo = PhotoImage(file = r"C:\Users\Desktop\icon.png") 
b.pack()
def button_click():
    score += 1

   
#while lives > 0:
    #btn = tt.Button(top, image="mole.png", command=button_click)
    
    

top.mainloop()

