import tkinter as tk
from tkinter import messagebox

# login reading from file
def read_file():
    users = {}
    try:
        with open("users.txt", "r") as f:
            for line in f:
                line = line.strip()
                if "," in line:
                    username, password = line.split(",", 1)
                    users[username] = password
    except FileNotFoundError:
        pass
    return users

def write_file(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

def login():
    username = entry_user.get()
    password = entry_pass.get()
    
    if username == "" or password == "":
        messagebox.showwarning("Warning", "Please fill all fields!")
        return
    
    users = read_file()
    
    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome back, {username}!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")

def signup():
    username = entry_user.get()
    password = entry_pass.get()
    
    if username == "" or password == "":
        messagebox.showwarning("Warning", "Please fill all fields!")
        return
    
    users = read_file()
    
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        write_file(username, password)
        messagebox.showinfo("Success", f"Account created for {username}!")

def main():
    global entry_user, entry_pass
    
    tk.Label(root, text="Login System", font=("Arial", 16, "bold")).pack(pady=10)
    
    tk.Label(root, text="Username:").pack()
    entry_user = tk.Entry(root, width=30)
    entry_user.pack(pady=5)
    
    tk.Label(root, text="Password:").pack()
    entry_pass = tk.Entry(root, width=30, show="*")
    entry_pass.pack(pady=5)
    
    tk.Button(root, text="Login", width=15, bg="green", fg="white", command=login).pack(pady=5)
    tk.Button(root, text="Signup", width=15, bg="blue", fg="white", command=signup).pack(pady=5)

root = tk.Tk()
root.title("Login System")
root.geometry("300x250")
main()
root.mainloop()