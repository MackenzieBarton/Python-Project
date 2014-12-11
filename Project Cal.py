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
        self.display.grid(row=1, column=0, columnspan=3)
        self.text = Text(self.root, height=1, width=1)
        self.text.grid(row=1, column=3)
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
        Button(self.root, text="=", width=7, command=lambda: self.doMath("=")).grid(row=8, column=0)
        Button(self.root, text="MC", width=7, command=lambda: self.clearMemory()).grid(row=8, column=1)
        Button(self.root, text="MR", width=7, command=lambda: self.getMemory()).grid(row=8, column=2)
        Button(self.root, text="MS", width=7, command=lambda: self.setMemory()).grid(row=8, column=3)
        
#These are the function buttons     
        #Button(self.root, text="(", width=7, foreground="red", command=lambda: self.addNumber("(")).grid(row=8, column=0)
        Button(self.root, text="+/-", width=7, foreground="red", command=lambda: self.invert()).grid(row=7, column=2)
        Button(self.root, text="X", width=7, foreground="red", command=lambda: self.doMath("*")).grid(row=4, column=3)
        Button(self.root, text="÷", width=7, foreground="red", command=lambda: self.doMath("/")).grid(row=5, column=3)
        Button(self.root, text="-", width=7, foreground="red", command=lambda: self.doMath("-")).grid(row=6, column=3)
        Button(self.root, text="+", width=7, foreground="red", command=lambda: self.doMath("+")).grid(row=7, column=3)
        Button(self.root, text="Clear", width=7, command=lambda:self.clear("all")).grid(row=3, column=3)
        Button(self.root, text="Delete", width=7, command=lambda:self.clear("1")).grid(row=3, column=2)   
        self.display.insert(END, '0')
        self.operator = "="
        self.value = 0
        self.printed = True
        self.memory = 0

    def invert(self):
        temp = -float(self.display.get())
        self.display.delete(0, END)
        if temp == int(temp):
            self.display.insert(END, int(temp))
        else:
            self.display.insert(END, temp)
    def addNumber(self, char):
        if self.printed == True:
            temp = "0"
        else:
            temp = self.display.get()
        self.printed = False
        if (temp == '0') and char != '.':
            temp = ""
        if self.dot == True and char == '.':
            self.display.delete(0, END)
            self.display.insert(END, temp)
        if char == '.':
            self.dot = True
        temp = temp + char
        self.display.delete(0, END)
        self.display.insert(END, temp)
        
    
    def doMath(self, oper):
        temp = self.display.get()

        self.value = float(temp)
        self.operator = oper
        self.clear("all") 

    #def AddFunction():
    #def doingEquation():
    #def Equals():
   # def clear():
   # def memory():

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
        if self.operator == '=':
            self.value = self.value2
        self.display.delete(0, END)
        if self.value == int(self.value):
            self.display.insert(END, int(self.value))
        else:
            self.display.insert(END, self.value)
        self.printed = True
        self.operator = oper
        
    def clear(self, mode):
        if mode == 'all':
            self.display.delete(0, END)
            self.display.insert(END, '0')
            self.dot = False
            self.value = 0
            self.printed = True
            self.operator = '='
        else:
            temp = self.display.get()
            self.display.delete(0, END)
            temp = temp[:-1]
            self.display.insert(END, temp)
  
    def setMemory(self):
        self.memory = float(self.display.get())
        self.printed = True
        if self.memory == 0:
            self.text.delete(1.0, END)
        else:
            self.text.delete(1.0, END)
            self.text.insert(INSERT,"M")
    def getMemory(self):
        self.display.delete(0, END)
        if self.memory == int(self.memory):
            self.display.insert(END, int(self.memory))
        else:
            self.display.insert(END, self.memory)
    def clearMemory(self):
        self.memory = 0
        self.text.delete(1.0, END)
        


root = Tk()
Calculator = calculator(root)
root.mainloop()


#calculator()
