from tkinter import *


window = Tk()
window.title("Calculator_App_with_Tkinter")
window.geometry("450x350")
window.configure(bg="lightgrey")
label = Label(window, text="This Calculator is made using Tkinter!", font=("Arial", 16))
label.pack(pady=10)



e = Entry(window, width=26, borderwidth=5, font=("Lucida Console", 20))
e.place(x=10, y=50)

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b = Button(window, text="1", width=10, height=2, command=lambda: click(1), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=10, y=100)

b = Button(window, text="2", width=10, height=2, command=lambda: click(2), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=120, y=100)

b = Button(window, text="3", width=10, height=2, command=lambda: click(3), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=230, y=100)

b = Button(window, text="4", width=10, height=2, command=lambda: click(4), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=10, y=140)

b = Button(window, text="5", width=10, height=2, command=lambda: click(5), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=120, y=140)

b = Button(window, text="6", width=10, height=2, command=lambda: click(6), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=230, y=140)

b = Button(window, text="7", width=10, height=2,command=lambda: click(7), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=10, y=180)

b = Button(window, text="8", width=10, height=2, command=lambda: click(8), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=120, y=180)

b = Button(window, text="9", width=10, height=2, command=lambda: click(9), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=230, y=180)

b = Button(window, text="0", width=20, height=2, command= lambda: click(0), font=("Lucida Console", 10, "bold"), bg='black',fg='white')
b.place(x=10, y=220)

def add():
    n1 = e.get()
    global math
    math = 'addition'
    global i
    i = int(n1)
    e.delete(0, END)

def sub():
    n1 = e.get()
    global math
    math = 'substraction'
    global i
    i = int(n1)
    e.delete(0, END)

def multiply():
    n1 = e.get()
    global math
    math = 'multiplication'
    global i
    i = int(n1)
    e.delete(0, END)

def div():
    n1 = e.get()
    global math
    math = 'division'
    global i
    i = int(n1)
    e.delete(0, END)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, i + int(n2))
    elif math == 'substraction':
        e.insert(0, i - int(n2))
    elif math == 'multiplication':
        e.insert(0, i * int(n2))
    elif math == 'division':
        e.insert(0, i / int(n2))

def clear():
    e.delete(0, END)

b = Button(window, text="+", width=10 , height=2, command=add, font=("Lucida Console", 10, "bold"), bg='orange',fg='white')
b.place(x=340, y=100)

b = Button(window, text="-", width=10 , height=2, command=sub, font=("Lucida Console", 10, "bold"), bg='orange',fg='white')
b.place(x=340, y=140)

b = Button(window, text="*", width=10 , height=2, command=multiply, font=("Lucida Console", 10, "bold"), bg='orange',fg='white')
b.place(x=340, y=180)

b = Button(window, text="/", width=10 , height=2, command=div, font=("Lucida Console", 10, "bold"), bg='orange',fg='white')
b.place(x=340, y=220)

b = Button(window, text="=", width=10 , height=2, command= equal, font=("Lucida Console", 10, "bold"), bg='orange',fg='white')
b.place(x=340, y=260)

b = Button(window, text="Clear", width=20, height=2, command=clear, font=("Lucida Console", 10, "bold"), bg='grey',fg='white')
b.place(x=10, y=260)


mainloop()