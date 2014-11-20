from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

baseCal = drawpad.create_rectangle(280,100,520,450)
screen = drawpad.create_rectangle(300,120,500,240)
















root.mainloop()