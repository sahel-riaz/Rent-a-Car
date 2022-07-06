#booking interface....


import tkinter as tk
from  tkinter import *


root=tk.Tk()
root.title('BOOK NOW')

def configureWindow(window,rows,columns):
        for i in range(rows):
            window.rowconfigure(i,weight=1)
        for j in range(columns):
            window.columnconfigure(j,weight=1)


            

l1=StringVar()
l2=StringVar()
l3=StringVar()
l4=StringVar()
l5=StringVar()
l6=StringVar()
l7=StringVar()
l8=StringVar()
l9=StringVar()
l10=StringVar()


def inft():
    na1=l1.get()
    nu2=l2.get()
    em3=l3.get()
    ad4=l4.get()
    print(na1,nu2,em3,ad4)



l_1=Label(root, text="Name:",)
l_1.grid(row=5, column=5)
name=Entry(root,textvar=l1)
name.grid(row=6,column=5)

l_2=Label(root, text="Number:")
l_2.grid(row=13, column=11)
numb=Entry(root,textvar=l2)
numb.grid(row=14, column=11)


l_3=Label(root, text="Email Id:")
l_3.grid(row=5, column=8)
email=Entry(root,textvar=l3)
email.grid(row=6, column=8)

l_9=Label(root, text="Age:")
l_9.grid(row=5, column=11)
age=Entry(root,textvar=l9)
age.grid(row=6, column=11)

l_10=Label(root, text="Car Name:")
l_10.grid(row=9, column=5)
cnam=Entry(root,textvar=l10)
cnam.grid(row=10, column=5)

l_5=Label(root, text="Date of Issue:")
l_5.grid(row=9, column=8)
dis=Entry(root,textvar=l5)
dis.grid(row=10, column=8)

l_6=Label(root, text="Date of Return:")
l_6.grid(row=9, column=11)
dret=Entry(root,textvar=l6)
dret.grid(row=10, column=11)

l_7=Label(root, text="Credit Card Number:")
l_7.grid(row=13, column=5)
cnum=Entry(root,textvar=l7)
cnum.grid(row=14, column=5)

l_8=Label(root, text="Passport Number:")
l_8.grid(row=13, column=8)
pnum=Entry(root,textvar=l8)
pnum.grid(row=14, column=8)



checkout=Button(root, text='CHECKOUT', command=inft)
checkout.grid(row=16, column=8)



configureWindow(root,20,20)


root.mainloop()


