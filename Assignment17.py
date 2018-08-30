#Question1
'''
import tkinter
from tkinter import *

root=Tk()
root.geometry("150x50")
root.title("Phone Directory")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist=Listbox(root, yscrollcommand=scrollbar.set) 
data={'Anoop':9464512112,'Shubham':7988620986,'Thakur':8894130776,'Abhinav':9459812455,'Abhishek':9464512112,'Shivam':7988620986,'Taniya':8894130776,'Abhilash':9459812455,'Appy':9464512112,'Akshay':7988620986,'Rana':8894130776,'Abhi':9459812455}
for key in data.keys():
    mylist.insert(END,"" +str(key))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()

'''
#Question2
'''
import tkinter
from tkinter import *

data={'Anoop':9464512112,'Shubham':7988620986,'Thakur':8894130776,'Abhinav':9459812455,'Abhishek':9464512112,'Shivam':7988620986,'Taniya':8894130776,'Abhilash':9459812455,'Appy':9464512112,'Akshay':7988620986,'Rana':8894130776,'Abhi':9459812455}
def insert():
    k=e1.get()
    v=e2.get()
    data[k]=v
    mylist.insert(END,k)
    print(data)

root=Tk()
e1=Entry(root)
e1.pack()
e2=Entry(root)
e2.pack()
b=Button(root,text="INSERT ITEMS",command=insert)
b.pack()
root.geometry("150x150")
root.title("Phone Directory")    
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist=Listbox(root, yscrollcommand=scrollbar.set)
for key in data.keys():
    mylist.insert(END,"" +str(key))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()

'''
