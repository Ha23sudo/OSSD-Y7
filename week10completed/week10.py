import tkinter as tk


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
file.write(username + "," + password + "\n")


# Login function
def login():
username = username_entry.get()
password = password_entry.get()

users = read_file()

for user in users:
stored_username, stored_password = user.strip().split(",")

if username == stored_username and password == stored_password:
print("Login successful")
return

print("Invalid username or password")


# Signup function
def signup():
username = username_entry.get()
password = password_entry.get()

write_file(username, password)

print("Signup successful")


# Main window
root = tk.Tk()
root.title("Login System")
root.geometry("400x300")

# Username
username_label = tk.Label(root, text="Username")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

# Password
password_label = tk.Label(root, text="Password")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Buttons
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=5)

signup_button = tk.Button(root, text="Signup", command=signup)
signup_button.pack(pady=5)

root.mainloop()