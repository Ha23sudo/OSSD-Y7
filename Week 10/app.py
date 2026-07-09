import tkinter as tk
from tkinter import messagebox
import os

# login reading from file
USER_FILE = "users.txt"


def read_file():
    """Read all users from the file and return them as a dict {username: password}."""
    users = {}
    if not os.path.exists(USER_FILE):
        return users

    with open(USER_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if ":" in line:
                username, password = line.split(":", 1)
                users[username] = password
    return users


def write_file(username, password):
    """Append a new user record to the file."""
    with open(USER_FILE, "a") as file:
        file.write(f"{username}:{password}\n")


def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Username and password cannot be empty!")
        return

    users = read_file()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome back, {username}!")
    elif username in users:
        messagebox.showerror("Login Failed", "Incorrect password.")
    else:
        messagebox.showerror("Login Failed", "User not found. Please sign up first.")


def signup():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Username and password cannot be empty!")
        return

    users = read_file()

    if username in users:
        messagebox.showerror("Signup Failed", "Username already exists.")
        return

    write_file(username, password)
    messagebox.showinfo("Success", "Account created successfully! You can now log in.")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def main():
    root.mainloop()


root = tk.Tk()
root.title("Login System")
root.geometry("300x250")

# Widgets
tk.Label(root, text="Username").pack(pady=(20, 0))
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", width=15, command=login).pack(pady=10)
tk.Button(root, text="Sign Up", width=15, command=signup).pack(pady=5)

if __name__ == "__main__":
    main()