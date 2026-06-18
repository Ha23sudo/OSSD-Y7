import tkinter as tk
from tkinter import messagebox

FILE = "users.txt"

def read_file():
    users = {}
    try:
        with open(FILE, "r") as f:
            for line in f:
                line = line.strip()
                if "," in line:
                    u, p = line.split(",", 1)
                    users[u] = p
    except FileNotFoundError:
        pass
    return users

def write_file(username, password):
    users = read_file()
    users[username] = password
    with open(FILE, "w") as f:
        for u, p in users.items():
            f.write(f"{u},{p}\n")

def login():
    u = entry_user.get().strip()
    p = entry_pass.get().strip()
    users = read_file()
    if u in users and users[u] == p:
        messagebox.showinfo("Success", f"Welcome, {u}!")
    else:
        messagebox.showerror("Error", "Wrong username or password.")

def signup():
    u = entry_user.get().strip()
    p = entry_pass.get().strip()
    if u == "" or p == "":
        messagebox.showerror("Error", "Fields cannot be empty.")
        return
    users = read_file()
    if u in users:
        messagebox.showerror("Error", "Username already exists.")
    else:
        write_file(u, p)
        messagebox.showinfo("Success", "Account created!")

def main():
    global entry_user, entry_pass

    tk.Label(root, text="Username").pack(pady=5)
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Password").pack(pady=5)
    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()

    tk.Button(root, text="Login",  command=login).pack(pady=5)
    tk.Button(root, text="Sign Up", command=signup).pack()

root = tk.Tk()
root.title("Login System")
root.geometry("250x200")

main()
root.mainloop()