#(Q.1)- Create a dict with name and mobile number.
# Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

from tkinter import *

window = Tk()
window.title('App1')
window.maxsize(300,65)
listbox = Listbox(window)
listbox.pack(side=LEFT,fill=Y)

d={'Vibhor':96710,'Vinay':63513,'Rahul':89302,'Yash':88973,'Mahi':98131}
for k in d.keys():
    listbox.insert(END,k)

scroll = Scrollbar(window,command=listbox.yview)
scroll.pack(side=RIGHT,fill=Y)
listbox.config(yscrollcommand=scroll.set)
label = Label(window,text="Window",bg="pink")
label.pack()


#(Q.2)- In the same tkinter file as created above, create a function to insert items into the dictionary.

def show():
    k = listbox.get(ACTIVE)
    v = d[k]
    label1.config(text=k)
    label2.config(text=v)

def insert():
    k = box1.get()
    v = box2.get()
    d[k] = v
    listbox.insert(END,k)
    print(d)

window = Tk()
window.title('App2')
window.maxsize(350,150)
listbox = Listbox(window)
listbox.pack(side=LEFT,fill=Y)

d={'Vibhor':96710,'Vinay':63513,'Rahul':89302,'Yash':88973,'Mahi':98131}
for k in d.keys():
    listbox.insert(END,k)

scroll = Scrollbar(window,command=listbox.yview)
scroll.pack(side=RIGHT,fill=Y)
listbox.config(yscrollcommand=scroll.set)
label1 = Label(window,text="Name",bg="pink",font=10)
label1.pack()
label2 = Label(window,text="Number",bg="green",font=10)
label2.pack()

button1 = Button(window,text="Show",command=show)
button1.pack()

box1 = Entry(window)
box1.pack()
box2 = Entry(window)
box2.pack()

button2 = Button(window,text="Insert",command=insert)
button2.pack()

window.mainloop()