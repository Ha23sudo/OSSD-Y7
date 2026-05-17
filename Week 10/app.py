import tkinter as tk
from tkinter import messagebox

FILE_NAME = "users.txt"
# Read users from file
def read_file():
    users = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 2:
                    username, password = data
                    users[username] = password

    except FileNotFoundError:
        open(FILE_NAME, "w").close()

    return users

def write_file(username, password):
    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{password}\n")

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

#Home Page
def home_page(username):

    clear_window()
    title = tk.Label(
        root,
        text=f"Welcome {username}",
        font=("Arial", 18)
    )
    title.pack(pady=20)

    btn1 = tk.Button(
        root,
        text="Option 1",
        width=20
    )
    btn1.pack(pady=5)

    btn2 = tk.Button(
        root,
        text="Option 2",
        width=20
    )
    btn2.pack(pady=5)

    btn3 = tk.Button(
        root,
        text="Option 3",
        width=20
    )
    btn3.pack(pady=5)

    logout_btn = tk.Button(
        root,
        text="Logout",
        width=20,
        command=login_page
    )
    logout_btn.pack(pady=20)

#Login Function
def login():

    username = username_entry.get().strip()
    password = password_entry.get().strip()

    users = read_file()
    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    if username not in users:
        messagebox.showerror("Error", "Account does not exist")
        return

    if users[username] != password:
        messagebox.showerror("Error", "Wrong Credentials")
        return

    messagebox.showinfo("Success", "Login Successful")

    home_page(username)

#Sigup Function
def signup():
    username = signup_username_entry.get().strip()
    password = signup_password_entry.get().strip()

    users = read_file()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    if username in users:
        messagebox.showerror("Error", "Username already exists")
        return

    write_file(username, password)

    messagebox.showinfo("Success", "Account Created Successfully")

    login_page()

def signup_page():

    global signup_username_entry
    global signup_password_entry
    clear_window()

    title = tk.Label(
        root,
        text="Signup Page",
        font=("Arial", 18)
    )
    title.pack(pady=20)

    username_label = tk.Label(root, text="Create Username")
    username_label.pack(pady=5)

    signup_username_entry = tk.Entry(root, width=25)
    signup_username_entry.pack(pady=5)

    password_label = tk.Label(root, text="Create Password")
    password_label.pack(pady=5)

    signup_password_entry = tk.Entry(root, show="*", width=25)
    signup_password_entry.pack(pady=5)

    signup_btn = tk.Button(
        root,
        text="Signup",
        width=20,
        command=signup
    )
    signup_btn.pack(pady=10)

    back_btn = tk.Button(
        root,
        text="Back to Login",
        width=20,
        command=login_page
    )
    back_btn.pack(pady=5)

#Login Page
def login_page():

    global username_entry
    global password_entry

    clear_window()
    title = tk.Label(
        root,
        text="Login System",
        font=("Arial", 18)
    )
    title.pack(pady=20)

    username_label = tk.Label(root, text="Username")
    username_label.pack(pady=5)

    username_entry = tk.Entry(root, width=25)
    username_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password")
    password_label.pack(pady=5)

    password_entry = tk.Entry(root, show="*", width=25)
    password_entry.pack(pady=5)

    login_btn = tk.Button(
        root,
        text="Login",
        width=20,
        command=login
    )
    login_btn.pack(pady=10)

    signup_btn = tk.Button(
        root,
        text="Sign Up",
        width=20,
        command=signup_page
    )
    signup_btn.pack(pady=5)

#Main Window
root = tk.Tk()
root.title("Rohan Ahmed - Login System")
root.geometry("350x350")

login_page()
root.mainloop()