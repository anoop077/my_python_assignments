#Question1
'''
import tkinter
from tkinter import *
root=Tk()
root.geometry("800x800")
root.title("GUI 1st Question")

lbl=Label(root,text='Hello World..!!!', font=('ALGERIAN', 40, 'bold'),bd=10)
lbl.pack()
button = Button(root, 
                   text="EXIT", 
                   fg="red",
                   command=quit)
button.pack()

root.mainloop()

'''
#Question2
'''
from tkinter import *
window = Tk()
window.title("GUI 2nd Question")
window.geometry('350x200')
lbl = Label(window, text="Hello World....!!!")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()

'''
#Question3
'''
import tkinter
from tkinter import *
root=Tk()
root.geometry("800x800")
root.title("GUI 3rd Question")
f=Frame(root,height=400, width=800,bg='cyan')
f.pack()

lbl=Label(f,text='Hello World..!!!', font=('ALGERIAN', 40, 'bold'),bd=10)
lbl.pack()
button = Button(root, 
                   text="EXIT", 
                   fg="red",
                   command=quit)
button.pack()
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(root, text="Click Me", command=clicked)
btn.pack()

root.mainloop()

'''
#Question4
'''
from tkinter import *

def show():
   print("Your status: %s" % (entry.get()))

master = Tk()
Label(master, text="Enter your Status.").grid(row=0)


entry = Entry(master)

entry.grid()


btn=Button(master, text='Show', command=show)
btn.grid()

mainloop( )

'''
