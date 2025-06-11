import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkFont

class PizzaOrderGUI:
    # --- Class-level constants for styling ---
    BG_COLOR = "#ffffff"
    TEXT_COLOR_PRIMARY = "#1f2937"  # Darker gray for titles/headers
    TEXT_COLOR_SECONDARY = "#4b5563"


pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")