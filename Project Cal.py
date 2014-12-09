# -*- coding: utf-8 -*-
from Tkinter import *
class calculator:
    def __init__(self,master):
        self.root = Tk()
        self.menu = Menu(self.root)
        self.menu.add_command(label="Quit", command=self.root.destroy) 
        self.root.config(menu=self.menu)
        self.root.title("Calculator")
        self.display = Entry(self.root)
        self.display.grid(row=1, column=0, columnspan=5)
        self.dot = False
        self.equationEnd = False
#These are the buttons for 0-9
# 'Lambda' is a construction that allows python to use anonymous fuctions that are not bound to a name
        Button(self.root, text="1", width=7, foreground="blue", command=lambda: self.addNumber("1")).grid(row=4, column=0)
        Button(self.root, text="2", width=7, foreground="blue", command=lambda: self.addNumber("2")).grid(row=4, column=1)
        Button(self.root, text="3", width=7, foreground="blue", command=lambda: self.addNumber("3")).grid(row=4, column=2)
        Button(self.root, text="4", width=7, foreground="blue", command=lambda: self.addNumber("4")).grid(row=5, column=0)
        Button(self.root, text="5", width=7, foreground="blue", command=lambda: self.addNumber("5")).grid(row=5, column=1)
        Button(self.root, text="6", width=7, foreground="blue", command=lambda: self.addNumber("6")).grid(row=5, column=2)
        Button(self.root, text="7", width=7, foreground="blue", command=lambda: self.addNumber("7")).grid(row=6, column=0)
        Button(self.root, text="8", width=7, foreground="blue", command=lambda: self.addNumber("8")).grid(row=6, column=1)
        Button(self.root, text="9", width=7, foreground="blue", command=lambda: self.addNumber("9")).grid(row=6, column=2)
        Button(self.root, text="0", width=7, foreground="blue", command=lambda: self.addNumber("0")).grid(row=7, column=1)
#Buttons for decimal and equals
        Button(self.root, text=".", width=5, command=lambda: self.addNumber(".")).grid(row=7, column=0)
        Button(self.root, text="=", width=12, command=lambda: self.Equals()).grid(row=8, column=2, columnspan=2)
#These are the function buttons     
        #Button(self.root, text="(", width=7, foreground="red", command=lambda: self.addNumber("(")).grid(row=8, column=0)
        #Button(self.root, text=")", width=7, foreground="red", command=lambda: self.addNumber(")")).grid(row=8, column=1)
        Button(self.root, text="X", width=7, foreground="red", command=lambda: self.doMath("*")).grid(row=4, column=3)
        Button(self.root, text="÷", width=7, foreground="red", command=lambda: self.doMath("/")).grid(row=5, column=3)
        Button(self.root, text="-", width=7, foreground="red", command=lambda: self.doMath("-")).grid(row=6, column=3)
        Button(self.root, text="+", width=7, foreground="red", command=lambda: self.doMath("+")).grid(row=7, column=3)
        Button(self.root, text="Clear", width=7, command=lambda:self.clear("all")).grid(row=3, column=3)
        Button(self.root, text="Delete", width=7, command=lambda:self.clear("1")).grid(row=3, column=2)   
        self.display.insert(END, '0')

    #def addingNumbers():
    def addNumber(self, char):
        temp = self.display.get()
        if (temp == '0') and char != '.':
            self.display.delete(0)
        if self.dot == True and char == '.':
            return
        if char == '.':
            self.dot = True
        self.display.insert(END, char)
    
    def doMath(self, oper):
        temp = self.display.get()
        self.value = float(temp)
        self.operator = oper
        self.clear("all") 

    #def doingEquation()
    def Equals(self):
        temp = self.display.get()
        self.value2 = float(temp)
        if self.operator == '+':
            self.value = self.value + self.value2
        if self.operator == '-':
            self.value = self.value - self.value2
        if self.operator == '*':
            self.value = self.value * self.value2
        if self.operator == '/':
            self.value = self.value / self.value2
        self.display.delete(0, END)
        self.display.insert(END, self.value)
        
        
    def clear(self, mode):
        if mode == 'all':
            self.display.delete(0, END)
            self.display.insert(END, '0')
            self.dot = False
        else:
            temp = self.display.get()
            self.display.delete(0, END)
            temp = temp[:-1]
            self.display.insert(END, temp)
  
  #def memory():

root = Tk()
Calculator = calculator(root)
root.mainloop()


#calculator()