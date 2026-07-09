import tkinter as tk
# login reading from file
def read_file():
    file = open("users.txt", "r")
    data = file.readlines()
    file.close()
    return data


def write_file(username, password):
    file = open("users.txt", "a")
    file.write(username + "," + password + "\n")
    file.close()
    

def login():
    username = username_entry.get()
    password = password_entry.get()

    data = read_file()

    for line in data:
        user, pwd = line.strip().split(",")

        if username == user and password == pwd:
            print("Login Successful")
            return

    print("Invalid Username or Password")

def signup():

    username = username_entry.get()
    password = password_entry.get()

    write_file(username, password)

    print("Signup Successful")


root = tk.Tk()
root.title("Login System")    
tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack()
tk.Button(root, text="Signup", command=signup).pack()

root.mainloop()
