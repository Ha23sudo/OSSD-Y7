import tkinter as tk
from tkinter import messagebox


# Read users from file
def read_file():
    try:
        with open("users.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


# Write a new user to file
def write_file(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")


# Login function
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter username and password")
        return

    users = read_file()

    for user in users:
        try:
            stored_username, stored_password = user.strip().split(",")
        except ValueError:
            continue

        if username == stored_username and password == stored_password:
            messagebox.showinfo("Success", "Login Successful!")
            return

    messagebox.showerror("Failed", "Invalid Username or Password")


# Signup function
def signup():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter username and password")
        return

    users = read_file()

    # Check if username already exists
    for user in users:
        try:
            stored_username, _ = user.strip().split(",")
        except ValueError:
            continue

        if username == stored_username:
            messagebox.showerror("Error", "Username already exists")
            return

    write_file(username, password)
    messagebox.showinfo("Success", "Signup Successful!")

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Main Window
root = tk.Tk()
root.title("Login System")
root.geometry("400x300")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="Login & Signup System",
    font=("Arial", 16, "bold")
)
heading.pack(pady=10)

# Username
username_label = tk.Label(root, text="Username")
username_label.pack()

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Password
password_label = tk.Label(root, text="Password")
password_label.pack()

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Buttons
login_button = tk.Button(
    root,
    text="Login",
    width=15,
    command=login
)
login_button.pack(pady=10)

signup_button = tk.Button(
    root,
    text="Signup",
    width=15,
    command=signup
)
signup_button.pack()

# Run GUI
root.mainloop()