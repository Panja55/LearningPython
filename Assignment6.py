from tkinter import *

root=Tk()
root.geometry("150x200")
entry=Entry(root,bg="white",width=22,borderwidth=3,relief="solid",fg="black")
entry.place(x=5,y=5)

def click(num):
    res=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(res)+str(num))

def clear():
    entry.delete(0,END)

def add():
    n1=entry.get()
    entry.delete(0,END)
    global operation
    operation = 'Add'
    global num1
    num1=int(n1)

def sub():
    n1 = entry.get()
    entry.delete(0, END)
    global operation
    operation = 'Sub'
    global num1
    num1 = int(n1)

def mult():
    n1 = entry.get()
    entry.delete(0, END)
    global operation
    operation = 'Mult'
    global num1
    num1 = int(n1)

def div():
    n1 = entry.get()
    entry.delete(0, END)
    global operation
    operation = 'Div'
    global num1
    num1 = int(n1)

def eq():
    n2 = entry.get()
    entry.delete(0, END)
    if operation == 'Add':
        entry.insert(0,num1 + int(n2))
    elif operation == 'Sub':
        entry.insert(0, num1 - int(n2))
    elif operation == 'Mult':
        entry.insert(0, num1 * int(n2))
    elif operation == 'Div':
        if int(n2) == 0:
            entry.insert(0, "DIVISION BY ZERO")
        else :
            entry.insert(0, num1 / int(n2))


b=Button(root,width=5,text="1",command=lambda:click(1))
b.place(x=5,y=30)
b=Button(root,width=5,text="2",command=lambda:click(2))
b.place(x=50,y=30)
b=Button(root,width=5,text="3",command=lambda:click(3))
b.place(x=95,y=30)
b=Button(root,width=5,text="4",command=lambda:click(4))
b.place(x=5,y=55)
b=Button(root,width=5,text="5",command=lambda:click(5))
b.place(x=50,y=55)
b=Button(root,width=5,text="6",command=lambda:click(6))
b.place(x=95,y=55)
b=Button(root,width=5,text="7",command=lambda:click(7))
b.place(x=5,y=80)
b=Button(root,width=5,text="8",command=lambda:click(8))
b.place(x=50,y=80)
b=Button(root,width=5,text="9",command=lambda:click(9))
b.place(x=95,y=80)
b=Button(root,width=5,text="0",command=lambda:click(0))
b.place(x=5,y=105)
b=Button(root,width=5,text="+",command=add)
b.place(x=50,y=105)
b=Button(root,width=5,text="-",command=sub)
b.place(x=95,y=105)
b=Button(root,width=5,text="*",command=mult)
b.place(x=5,y=130)
b=Button(root,width=5,text="/",command=div)
b.place(x=50,y=130)
b=Button(root,width=5,text="Clear",command=clear)
b.place(x=95,y=130)
b=Button(root,width=18,text="=",command=eq)
b.place(x=5,y=155)


mainloop()