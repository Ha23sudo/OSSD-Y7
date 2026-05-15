import tkinter as tk
from tkinter import messagebox

# Read users from file
def read_file():
    users = {}  # create empty dictionary
    try:
        file = open("users.txt", "r")  # open file
        for line in file:
            line = line.strip()  # remove extra spaces
            if "," in line:
                username, password = line.split(",")  # separate username and password
                users[username] = password
        file.close()
    except FileNotFoundError:
        pass 
    return users

# Write new user into file
def write_file(username, password):
    file = open("users.txt", "a")  # "a" means append - old data will not be removed
    file.write(username + "," + password + "\n")
    file.close()


def login():
    username = entry_username.get()  
    password = entry_password.get()

    # if left empty
    if username == "" or password == "":
        messagebox.showwarning("Empty", "Please enter both username and password!")
        return

    users = read_file()  

    # check if username and password are correct
    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome, {username}! Login successful!")
    else:
        messagebox.showerror("Error", "Incorrect username or password!")

def signup():
    username = entry_username.get()
    password = entry_password.get()

    # if left empty
    if username == "" or password == "":
        messagebox.showwarning("Empty", "Please enter both username and password!")
        return

    users = read_file()

    # check if username already exists
    if username in users:
        messagebox.showerror("Error", "This username already exists!")
    else:
        write_file(username, password)  # save new user
        messagebox.showinfo("Success", "Account created! Now login.")



def main():
    # Labels
    label_title = tk.Label(root, text="Login System", font=("Arial", 18, "bold"))
    label_title.pack(pady=10)

    label_user = tk.Label(root, text="Username:")
    label_user.pack()

    global entry_username
    entry_username = tk.Entry(root, width=30)
    entry_username.pack(pady=5)

    label_pass = tk.Label(root, text="Password:")
    label_pass.pack()

    global entry_password
    entry_password = tk.Entry(root, width=30, show="*")  # show="*" means dots will appear
    entry_password.pack(pady=5)

    # Buttons
    btn_login = tk.Button(root, text="Login", width=15, command=login)
    btn_login.pack(pady=5)

    btn_signup = tk.Button(root, text="Signup", width=15, command=signup)
    btn_signup.pack(pady=5)



root = tk.Tk()
root.title("Login System")
root.geometry("300x250")  # window size

main()  # create UI

root.mainloop()  # keep window open