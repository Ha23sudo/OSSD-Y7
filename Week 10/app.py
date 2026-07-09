import tkinter as tk
from tkinter import messagebox

# Read users from file
def read_file():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass
    return users

# Write a new user to file
def write_file(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

# Login function
def login():
    username = entry_username.get()
    password = entry_password.get()

    users = read_file()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# Signup function
def signup():
    username = entry_username.get()
    password = entry_password.get()

    users = read_file()

    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        write_file(username, password)
        messagebox.showinfo("Success", "Account Created Successfully!")

# Main GUI
def main():
    global entry_username, entry_password

    tk.Label(root, text="Username").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    tk.Button(root, text="Login", command=login).pack(pady=5)
    tk.Button(root, text="Sign Up", command=signup).pack(pady=5)

# Create window
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

main()

root.mainloop()