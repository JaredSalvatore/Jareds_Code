#Yo.
# Welcome to area calc.
from tkinter import *

root = Tk() (text= "Area Calculator")
def calculate_area():
    length = input("enter the length: ")
    width = input("enter the width: ")
    result = float(length) * float(width)
    return result
print (f'the area is: {calculate_area()}') 
root.pack()
root.mainloop()


