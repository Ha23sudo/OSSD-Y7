import tkinter as tk

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

entry = tk.Entry(root, width=25)
entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        tk.Button(button_frame, text=button, width=5, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(button_frame, text=button, width=5, command=lambda b=button: press(b)).grid(row=row, column=col)

    col += 1

    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Clear", command=clear).pack()

root.mainloop()