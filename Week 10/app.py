import tkinter as tk
from tkinter import messagebox
def read_file():
    
    pass
    try:
        with open("users.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
def write_file():
    pass
    try:
       user = username_entry.get()
    pwd = password_entry.get()
    with open("users.txt", "a") as file:
        file.write(f"{user},{pwd}\n")

def login():
    pass
    user = username_entry.get()
    pwd = password_entry.get()
    
    for record in read_file():
        if record.strip():  # Khali lines ko ignore karne ke liye
            stored_user, stored_pass = record.strip().split(",")
            if user == stored_user and pwd == stored_pass:
                messagebox.showinfo("Success", "Login Successful!")
                return
                
    messagebox.showerror("Error", "Invalid Username or Password")
def signup():
    pass    
    user = username_entry.get()
    pwd = password_entry.get()
    
    if not user or not pwd:
        messagebox.showwarning("Error", "Please fill all fields!")
        return

    for record in read_file():
        if record.strip():
            stored_user, _ = record.strip().split(",")
            if user == stored_user:
                messagebox.showerror("Error", "Username already exists!")
                return
                
    write_file()
    messagebox.showinfo("Success", "Signup Successful!")
def main():
    pass
    global username_entry, password_entry
    
    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()
    
    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    
    tk.Button(root, text="Login", command=login).pack(pady=5)
    tk.Button(root, text="Signup", command=signup).pack()
root = tk.Tk()
root.title("Login System")    

main()

root.mainloop()
