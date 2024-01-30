
# pip install tkinter
import sqlite3
from tkinter import * 
# pip install pyperclip
import pyperclip 
import random
from tkinter import filedialog
from tkinter import messagebox
import tkinter as ttk
import tkinter as tk
root = Tk()
root.geometry("700x330")
root.resizable(0,0)
root.title("OpenPasswordGen")
my_menu= Menu(root)
root.config(menu=my_menu)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='Icon.png'))

#Popups that will display.
#The popup for what this software is.
#Creating a database 
Database_init = sqlite3.connect("Passwords.db")
cursor = Database_init.cursor()

#Just creating a simple table.
cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, password TEXT)''')
Database_init.commit()
def About():
    root = Tk() 
    root.resizable(0,0)
    root.title("About")

    labelTitle = tk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="About:")
    label = tk.Label(root,font=("Ubuntu", 16,),anchor='center', text="This is a simple password generator for Linux!")


    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
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
def load_passwords_popup():
    def search_passwords(event=None):
        search_query = search_var.get()
        cursor.execute("SELECT password FROM passwords WHERE password LIKE ?", ('%' + search_query + '%',))
        update_passwords_display(cursor.fetchall())

    def update_passwords_display(passwords):
        for widget in passwords_entries_frame.winfo_children():
            widget.destroy()
        for password in passwords:
            frame = Frame(passwords_entries_frame)
            frame.pack(side="top", fill="x", pady=5)

            label = Label(frame, font=("Ubuntu", 14), text=password[0])
            label.pack(side="left", padx=10)

            copy_button = Button(frame, text="Copy", font=("Ubuntu", 12), bg="grey", activebackground='pink', command=lambda p=password[0]: pyperclip.copy(p))
            copy_button.pack(side="right", padx=10)

    popup = Toplevel(root)
    popup.title("All Passwords in Database")
    popup.geometry("700x400")
    popup.resizable(0,0)


    labelTitle = Label(popup, font=("Ubuntu", 18, "bold", "underline"), text="All Passwords:")
    labelTitle.pack(side="top", fill="x", pady=10)

    search_var = StringVar()
    search_entry = Entry(popup, textvariable=search_var, font=("Ubuntu", 14))
    search_entry.pack(side="top", fill="x", padx=10, pady=10)
    search_entry.bind('<KeyRelease>', search_passwords)

    # Main frame for passwords and scrollbar
    main_frame = Frame(popup)
    main_frame.pack(side=TOP, fill=BOTH, expand=True)
    

    # Canvas to attach the scrollbars
    canvas = Canvas(main_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Scrollbar on the right side, filling the y-axis
    scrollbar = Scrollbar(main_frame, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.config(yscrollcommand=scrollbar.set)

    # Horizontal scrollbar spanning the bottom of the popup
    scrollbar2 = Scrollbar(popup, orient='horizontal', command=canvas.xview)
    scrollbar2.pack(side=BOTTOM, fill=X)
    canvas.config(xscrollcommand=scrollbar2.set)

    # Frame inside the canvas for password entries
    passwords_entries_frame = Frame(canvas)
    canvas.create_window((0, 0), window=passwords_entries_frame, anchor='nw')

    # Update canvas scrollregion when the size of the frame changes
    passwords_entries_frame.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

    # Initial display of passwords
    cursor.execute("SELECT password FROM passwords")
    update_passwords_display(cursor.fetchall())


def save_database_password():
    password_save = passwrd.get().splitlines()
    for password in password_save:
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
    Database_init.commit()
    messagebox.showinfo("It worked", "Password saved.")

file_menu= Menu(my_menu,background="grey",activebackground="pink",border="6")

my_menu.add_cascade(label="About:",font=("Ubuntu",18),activebackground="pink", menu=file_menu)
file_menu.add_command(label="What is this software?",font=("Ubuntu",18),activebackground="pink",background="grey",command=About) 
file_menu.add_command(label="Who made this software?",font=("Ubuntu",18),activebackground="pink",background="grey",command=Who_made_Me) 
Database = Menu(my_menu,background="grey",activebackground="pink",border="6")

my_menu.add_cascade(label="Options:",font=("Ubuntu",18),activebackground="pink", menu=Database)
Database.add_command(label="Save to Database.",font=("Ubuntu",18),activebackground="pink",background="grey",command=save_database_password)
Database.add_command(label="Load Database.",font=("Ubuntu",18),activebackground="pink",background="grey",command=load_passwords_popup)

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
