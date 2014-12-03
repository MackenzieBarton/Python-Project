# -*- coding: utf-8 -*-
from Tkinter import *
class calculator:
    def __init__(self):
#These are the buttons for 0-9
# 'Lambda' 
     Button(self.root, text="1", width=5, foreground="blue", command=lambda: self.addNumber("1")).grid(row=4, column=0)
     Button(self.root, text="2", width=5, foreground="blue", command=lambda: self.addNumber("2")).grid(row=4, column=1)
     Button(self.root, text="3", width=5, foreground="blue", command=lambda: self.addNumber("3")).grid(row=4, column=2)
     Button(self.root, text="4", width=5, foreground="blue", command=lambda: self.addNumber("4")).grid(row=5, column=0)
     Button(self.root, text="5", width=5, foreground="blue", command=lambda: self.addNumber("5")).grid(row=5, column=1)
     Button(self.root, text="6", width=5, foreground="blue", command=lambda: self.addNumber("6")).grid(row=5, column=2)
     Button(self.root, text="7", width=5, foreground="blue", command=lambda: self.addNumber("7")).grid(row=6, column=0)
     Button(self.root, text="8", width=5, foreground="blue", command=lambda: self.addNumber("8")).grid(row=6, column=1)
     Button(self.root, text="9", width=5, foreground="blue", command=lambda: self.addNumber("9")).grid(row=6, column=2)
     Button(self.root, text="0", width=5, foreground="blue", command=lambda: self.addNumber("0")).grid(row=7, column=1)
#Buttons for decimal and equals
     Button(self.root, text=".", width=5, command=lambda: self.addNumber(".")).grid(row=7, column=0)
     Button(self.root, text="=", width=12, command=lambda: self.Equals()).grid(row=8, column=2, columnspan=2)
#These are the function buttons     
     Button(self.root, text="(", width=5, foreground="red", command=lambda: self.addNumber("(")).grid(row=8, column=0)
     Button(self.root, text=")", width=5, foreground="red", command=lambda: self.addNumber(")")).grid(row=8, column=1)
     Button(self.root, text="X", width=5, foreground="red", command=lambda: self.addNumber("x")).grid(row=4, column=3)
     Button(self.root, text="÷", width=5, foreground="red", command=lambda: self.addNumber("÷")).grid(row=5, column=3)
     Button(self.root, text="-", width=5, foreground="red", command=lambda: self.addNumber("-")).grid(row=6, column=3)
     Button(self.root, text="+", width=5, foreground="red", command=lambda: self.addNumber("+")).grid(row=7, column=3)
     Button(self.root, text="C", width=5, command=lambda:self.clear("all")).grid(row=3, column=3)
     Button(self.root, text="Del.", width=5, command=lambda:self.clear("1")).grid(row=3, column=2)   
mainloop()