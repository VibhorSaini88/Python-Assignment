#(Q.1)- Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

import tkinter
from tkinter import *
import sys
def display():
    print("Hello World!")
window = Tk()
window.title("My App")
frame1 = Frame(window,display())
bt = Button(window,text="EXIT",width=35,bg="red",command=sys.exit)
bt.pack()
window.mainloop()


#(Q.2)- Write a python program to in the same interface as above and create a action when the button is click it will display some text.

def show():
    print("I am in the CLI(Command Line Interface)!")
root = Tk()
root.title("My Text")
bt = Button(root,text="click here!",activebackground="green",width=30,height=10,command=show)
bt.place(x=1,y=1)
bt.pack()
root.mainloop()


#(Q.3)- Create a frame using tkinter swith any label text and two buttons.One to exit and other to change the label to some other text.
import sys
def show():
    print("text changed")
    label.config(text = "label changed..")
create = Tk()
label = Label(create,text="My Project",width=35,font='20',bg="purple",fg="white")
label.pack()
button1 = Button(create,text="Label changed",width=20,height=5,bg="red",activeforeground="blue" ,command = show)
button1.pack()
button2 = Button(create,text="Exit",width=10,height=2,activebackground="pink",command=sys.exit)
button2.pack()
create.mainloop()


#(Q.4)- Write a python program using tkinter interface to take an input in the GUI program and print it.
def show():
    print(entry.get())
root = Tk()
label = Label(root,text="Write Text->",font='5')
label.grid(row=0)
entry = Entry(root,width=30)
entry.grid(row=0,column=1)
label1 =Label(root,text="Terminate->",font='5')
label1.grid(row=1)
bt = Button(root,text="PRINT",width=15,bg="pink",fg="brown",command=show)
bt.grid(row=1,column=1)
root.mainloop()