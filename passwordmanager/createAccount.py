from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
from mysql.connector import Error
import bcrypt

from appscreen import MainScreen

class CreateAccount:

    def __init__(self, root):
        self.root = root

        root.geometry("600x500")
        root.title("Create Account")
        root.resizable(width=False, height=False)
        mainFrame = Frame(root, width=600, height=500, bg="#27dde3")
        mainFrame.pack()

        self.heading = Label(mainFrame, text="Create Account", font=("Times New Roman", 30), bg="#27dde3")
        self.heading.place(x=150, y=30)

        # label: username, password, email address, recovery question, recovery answer
        self.username_label = Label(mainFrame, text="username*:", font=("Times New Roman", 16), bg="#27dde3")
        self.username_label.place(x=50, y=100)
        self.password_label = Label(mainFrame, text="password*:", font=("Times New Roman", 16), bg="#27dde3")
        self.password_label.place(x=50, y=150)
        self.confirmp_label = Label(mainFrame, text="confirm password*:", font=("Times New Roman", 16), bg="#27dde3")
        self.confirmp_label.place(x=50, y=200)
        self.email_label = Label(mainFrame, text="email address:", font=("Times New Roman", 16), bg="#27dde3")
        self.email_label.place(x=50, y=250)
        self.recovery_q_label = Label(mainFrame, text="recovery question*:", font=("Times New Roman", 16), bg="#27dde3")
        self.recovery_q_label.place(x=50, y=300)
        self.recovery_a_label = Label(mainFrame, text="recovery answer*:", font=("Times New Roman", 16), bg="#27dde3")
        self.recovery_a_label.place(x=50, y=350)

        # entry field: username, password, email address, recovery question, recovery answer
        self.username_entry = Entry(mainFrame, font=("Times New Roman", 15))
        self.username_entry.place(x=250, y=100)
        self.password_entry = Entry(mainFrame, font=("Times New Roman", 15), show="*")
        self.password_entry.place(x=250, y=150)
        self.confirmp_entry = Entry(mainFrame, font=("Times New Roman", 15), show="*")
        self.confirmp_entry.place(x=250, y=200)
        self.email_entry = Entry(mainFrame, font=("Times New Roman", 15))
        self.email_entry.place(x=250, y=250)
        self.recovery_q_entry = Entry(mainFrame, font=("Times New Roman", 15))
        self.recovery_q_entry.place(x=250, y=300)
        self.recovery_a_entry = Entry(mainFrame, font=("Times New Roman", 15))
        self.recovery_a_entry.place(x=250, y=350)

        # buttons: submit; clear written text
        self.signup_button = Button(mainFrame, text="submit", font=("Times New Roman", 16), command=self.submit)
        self.signup_button.place(x=200, y=400)
        self.clear_button = Button(mainFrame, text="clear", font=("Times New Roman", 16), command=self.clear)
        self.clear_button.place(x=300, y=400)

    def clear(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.confirmp_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.recovery_q_entry.delete(0, END)
        self.recovery_a_entry.delete(0, END)

    def close(self):
        self.root.destroy()

    def callApp(self, usern):
        rt = Tk()
        c = MainScreen(rt, usern)
        self.close()

    def submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirmp_entry.get()
        email = self.email_entry.get()
        recovery_question = self.recovery_q_entry.get()
        recovery_answer = self.recovery_a_entry.get()

        if len(username) < 6 or len(password) < 8 or confirm_password == "" or recovery_question == "" or recovery_answer == "" or (password != confirm_password):
            messagebox.showerror("Details", "Enter valid details")
        else:
            try:
                with sql.connect(host="localhost", user="root", password="your sql password", database="passwords_manager") as mydb:
                    cursor = mydb.cursor()

                    # check if username exists in the database
                    cursor.execute("SELECT username from users WHERE username = %s", (username,))
                    existing_username = cursor.fetchone()

                    if existing_username is not None:
                        messagebox.showerror("Create Account", "Username already exists")
                    else:
                        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                        cursor.execute("INSERT INTO users(username, email, password, recovery_question, recovery_answer) VALUES(%s, %s, %s, %s, %s)",
                                       (username, email, hashed_password, recovery_question, recovery_answer))
                        mydb.commit()
                        print("Account created")

                        # save primary key
                        login_username = username
                        # start the main app
                        self.callApp(login_username)

            except Error as err:
                print(f"Error: {err}")

root = Tk()
cs = CreateAccount(root)
root.mainloop()
