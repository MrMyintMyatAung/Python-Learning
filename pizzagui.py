import tkinter as tk
from tkinter import messagebox

def place_order():
    """
    Processes the selected toppings and displays the order details.
    """
    requested_toppings = [topping.get() for topping in topping_vars if topping.get()]

    added = []
    not_available = []

    for topping in requested_toppings:
        if topping in available_toppings:
            added.append(topping)
        else:
            not_available.append(topping)

    message = ""
    if added:
        message += "Adding toppings: " + ", ".join(added) + "\n"
    if not_available:
        message += "Sorry, we don't have: " + ", ".join(not_available) + "\n"

    if not message:
        message = "You didn't select any toppings."

    message += "\nFinished making your pizza."
    messagebox.showinfo("Your Pizza Order", message)

# --- Main Window Setup ---
root = tk.Tk()
root.title("Pizza Topping Selector")
root.geometry("300x250")

# --- Available Toppings ---
available_toppings = [
    'mushrooms', 'olives', 'green peppers',
    'pepperoni', 'pineapple', 'extra cheese'
]

# --- GUI Elements ---
title_label = tk.Label(root, text="Select Your Toppings", font=("Helvetica", 16))
title_label.pack(pady=10)

topping_vars = []
for topping in available_toppings:
    var = tk.StringVar(value="")
    chk = tk.Checkbutton(root, text=topping.title(), variable=var, onvalue=topping, offvalue="")
    chk.pack(anchor='w', padx=20)
    topping_vars.append(var)

order_button = tk.Button(root, text="Place Order", command=place_order)
order_button.pack(pady=20)

# --- Run the application ---
root.mainloop()