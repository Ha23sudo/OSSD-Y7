import tkinter as tk
from tkinter import messagebox
# login reading from file
def read_file():
   f=open("user.txt","r")
   f.close()
def write_file():
    f=open("user.txt","a")
    f.write(entery.get()+" "+pas_entry.get()+"\n")
    f.close()

def login():
    f=open("user.txt","r")
    for i in f:
            n,pas=i.split()
            if entery.get()==n:
                 if  pas_entry.get()==pas:
                            messagebox.showinfo("login","Login successful")
                            f.close()
                            return
            
                 if pas_entry.get()!=pas:
                        messagebox.showinfo("login failed","enter correct password")
                        f.close()
                        return
            
    messagebox.showinfo("login faild","register first")
    f.close()
    return

def signup():
    write_file()
    messagebox.showinfo("signup","Signup successful")
    
    
root= tk.Tk()
root.title("Login System") 
root.geometry("400x440")
root.configure(bg="white")
main_name=tk.Label(root,text="Welcome to the Login System",font=("Comic Sans MS",18,"bold"),bg="white",fg="black")
main_name.pack()
name_l=tk.Label(root,text="Username :",bg="white",font=("Times New Roman",12,"bold"))
name_l.place(x=50,y=50)
entery=tk.Entry(root,bg="LIGHTBLUE",font=("Times New Roman",12))
entery.place(x=150,y=50)
pas_l=tk.Label(root,text="password :",bg="white",font=("Times New Roman",12,"bold"))
pas_l.place(x=50,y=75)
pas_entry=tk.Entry(root,show="*",bg="LIGHTBLUE",font=("Times New Roman",12))
pas_entry.place(x=150,y=75)
login_botten=tk.Button(root,text="Login",bg='lightblue',command=login)
login_botten.place(x=150,y=110)
signup_botten=tk.Button(root,text="Signup",bg="lightblue",command=signup)
signup_botten.place(x=220,y=110)
root.mainloop()
