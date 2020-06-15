import tkinter
from tkinter import *
import random
from tkinter import messagebox
from random import shuffle


all_list = ["apple", "ball", "cat", "dog", "egg", "fish", "grapes", "hat",
            "icecream", "jug", "kite", "lion", "mango", "nest", "owl", "pen"]

emp_list = []

for i in all_list:
    word = list(i)
    shuffle(word)
    emp_list.append(word)

'''
    if word in all_list:
        shuffle(word)
    else:
        emp_list.append(word)
'''
num = random.randint(0, len(emp_list))


def first():
    global emp_list, all_list, num
    lb1.configure(text=emp_list[num])


def check():
    global emp_list, all_list, num
    user_input = e1.get()
    if (user_input == all_list[num]):
        messagebox.showinfo("Congratulation", "Your all_list is correct")
        Reset()
    else:
        messagebox.showinfo("Wrong", "Better Luck Next Time")
        e1.delete(0, END)


def Reset():
    global emp_list, all_list, num
    num = random.randint(0, len(emp_list))
    lb1.configure(text=emp_list[num])
    e1.delete(0, END)


root = tkinter.Tk()
root.geometry("300x400")
root.title("JUMBLER")
root.configure(background="pink")

lb1 = Label(root, font="times 20", bg="pink")
lb1.pack(pady=30, ipady=10, ipadx=10)

all_list12 = StringVar()
e1 = Entry(root, textvariable=all_list, insertwidth=3,
           bg='yellow', bd=5, justify='center', font=('times', 15, 'bold'))
e1.pack(ipady=5, ipadx=5)

button1 = Button(root, padx=30, pady=10, bd=5, bg='cyan', fg='blue', font=(
    'arial', 10, 'bold'), text='Check', command=check)
button1.pack(pady=40)

button2 = Button(root, padx=30, pady=10, bd=5, bg='lightgreen', fg='green', font=(
    'arial', 10, 'bold'), text='Reset', command=Reset)
button2.pack()


first()
root.mainloop()
