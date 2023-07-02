
# pip install tkinter
from tkinter import * 
# pip install pyperclip
import pyperclip 
import random
from tkinter import filedialog
from tkinter import messagebox
import tkinter as ttk
import tkinter as tk
root = Tk()
root.geometry("700x300")
root.resizable(0,0)
root.title("OpenPasswordGen")
my_menu= Menu(root)
root.config(menu=my_menu)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='Icon.png'))

#Popups that will display.
#The popup for what this software is.
def About():
    root = Tk() 
    root.resizable(0,0)
    root.title("About")

    labelTitle = tk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="About:")
    label = tk.Label(root,font=("Ubuntu", 16,),anchor='center', text="This is a simple password generator for Linux!")


    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="grey",border=12,activebackground='pink', command = root.destroy)
    B1.pack()
#############
#This popup is used to show who created this software.
def Who_made_Me():
    root = Tk() 
    root.resizable(0,0)
    root.title("Who created this software:")

    labelTitle = tk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Who created this software:")
    label = tk.Label(root,font=("Ubuntu", 16,),anchor='center', text="Jonathan Steadman.")


    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="grey",border=12,activebackground='pink', command = root.destroy)
    B1.pack()
file_menu= Menu(my_menu,background="grey",activebackground="pink",border="6")

my_menu.add_cascade(label="About:",font=("Ubuntu",18),activebackground="pink", menu=file_menu)
file_menu.add_command(label="What is this software?",font=("Ubuntu",18),activebackground="pink",background="grey",command=About) 
file_menu.add_command(label="Who made this software?",font=("Ubuntu",18),activebackground="pink",background="grey",command=Who_made_Me) 

passwrd = StringVar()
passlen = IntVar()
passlen.set(0)
 
 
def generate():  # Function to generate the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)
 
# function to copy the passcode

 
def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)
# Labels
 
 
Label(root, text="Open source Password Generator!", font=" ubuntu 30 bold underline").pack()
Label(root, text="Enter how many characters do you want your password to be:", font="ubuntu 14 bold").pack(pady=3)
Entry(root, textvariable=passlen, font="ubuntu 15 bold").pack(pady=3)
Button(root, text="Click here to get the new password.", font="ubuntu 14 bold",border=2,activebackground='pink',command=generate).pack(pady=7)
Label(root, text="This is your new password:", font="ubuntu 14 bold").pack(pady=3)

Entry(root, textvariable=passwrd, font=("ubuntu", 15)).pack(pady=3)
Button(root, text="Click here to copy to your clipboard.",font="ubuntu 15 bold",border=2,activebackground='pink', command=copyclipboard).pack()
root.mainloop()