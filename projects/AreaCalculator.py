# This is the windowed version of my dope calculator
from tkinter import *
root = Tk()
thelabel = Label(root, text="Yo.", bg='red')
Length= Button(root, text= "length", bg='magenta')
Width= Button(root, text= "width", bg='Green')
PriceSquareFoot= Button(root, text= "Price Per Sq. Ft.", bg='White')

thelabel.pack()
Length.pack()
Width.pack()
PriceSquareFoot.pack()
root.mainloop() 