from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
from mysql.connector import Error
import bcrypt

from appscreen import MainScreen
from createAccount import CreateAccount

class LoginScreen:
    def __init__(self, root):
        # First Screen: login screen
        self.root = root
        root.geometry("600x500")
        root.title("Login")
        root.resizable(width=False, height=False)
        mainFrame = Frame(root, width=600, height=500, bg="#27dde3")
        mainFrame.pack()
        self.heading = Label(mainFrame, text="Login", font=("Times New Roman", 35), bg="#27dde3")
        self.heading.place(x=200, y=150)

        # logins label
        self.username_label = Label(root, text="username: ", font=("Times New Roman", 16), bg="#27dde3")
        self.username_label.place(x=100, y=280)
        self.password_label = Label(root, text="password: ", font=("Times New Roman", 16), bg="#27dde3")
        self.password_label.place(x=100, y=330)
        # logins entry
        self.username_entry = Entry(root, font=("Times New Roman", 16))
        self.username_entry.place(x=200, y=280)
        self.password_entry = Entry(root, font=("Times New Roman", 16), show="*")
        self.password_entry.place(x=200, y=330)

        self.submit_button = Button(root, text="login", font=("Times New Roman", 16), width=21, command=self.login)
        self.submit_button.place(x=200, y=380)
        self.signup_button = Button(root, text="create account", font=("Times New Roman", 16), command=self.callCreate)
        self.signup_button.place(x=334, y=430)

        self.resetLogin_button = Button(root, text="forgot logins", font=("Times New Roman", 16))
        self.resetLogin_button.place(x=200, y=430)

    def callCreate(self):
        rt = Tk()
        cs = CreateAccount(rt)
        self.close()

    def callApp(self, usern):
        rt = Tk()
        c = MainScreen(rt, usern)
        self.close()

    def close(self):
        self.root.destroy()

    def login(self):
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Login", "Enter your logins")
        else:
            mydb = None
            try:
                # Connect to the database
                with sql.connect(
                        host="localhost",
                        user="root",
                        password="your sql password",
                        database="passwords_manager") as mydb:

                    print("Database connection successful")
                    cursor = mydb.cursor()

                    # Query: Retrieve hashed password from the database
                    cursor.execute("SELECT password FROM users WHERE username = %s", (self.username_entry.get(),))
                    hashed_password = cursor.fetchone()

                    if hashed_password is None:
                        messagebox.showerror("Login Error", "Logins not found")
                    else:
                        # Check if the entered password matches the stored hashed password
                        if bcrypt.checkpw(self.password_entry.get().encode(), hashed_password[0].encode()):
                            print("Log in successful")
                            # Save primary key
                            login_username = self.username_entry.get()
                            # Call appscreen(root, login_username)
                            self.callApp(login_username)
                        else:
                            messagebox.showerror("Login Error", "Incorrect password")

            except Error as err:
                print(f"Error: {err}")
                messagebox.showerror("Database Error", "Error connecting to the database")

root = Tk()
ls = LoginScreen(root)
root.mainloop()

