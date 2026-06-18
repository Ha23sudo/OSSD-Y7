from Scrapper import get_car_data
from tkinter import ttk
import tkinter as tk

def display_data(car):
    #Get data from scrapper
    data = get_car_data(car)
    
    #Clear Text area
    text_area.delete(1.0, tk.END)  
    
    # Check if data is not empty
    if data:
        for item in data:
            text_area.insert(tk.END, f"Name: {item[0]} | Price: {item[1]}\n")
            text_area.insert(tk.END, "-"*40 + "\n") # Ek line lagane ke liye (optional)
    else:
        # If data not fetch 
        text_area.insert(tk.END, f"{car.capitalize()} ka data nahi mil saka. Shayad internet ya website ka masla hai.\n")

# GUI Setup
root = tk.Tk()
root.title("Car Price Scraper")
root.geometry("600x400")

# Dropdown Menu
cars = ['kia', 'honda', 'toyota', 'suzuki', 'hyundai']
dropdrown = ttk.Combobox(root, values=cars)
dropdrown.current(3) # Default 'suzuki' par set hoga
dropdrown.pack(pady=20)

# Button
find = tk.Button(root, text="Find Price", command=lambda: display_data(dropdrown.get()))
find.pack(pady=10)

# Text Area for output
text_area = tk.Text(root, height=15, width=70)
text_area.pack(pady=20)

# App ko chalane ke liye
root.mainloop()