from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import hashlib
import json

# Import custom modules
from modules.windows.recipe_list import show_recipe_list_window
from modules.windows.create_recipe import show_create_recipe_window
from modules.windows.customer_list import show_customer_list_window
from modules.helpers import format_effects, EFFECTS

# Open Database
with open("db.json", "r") as file:
    data = json.load(file)

# Check if the database is corrupted or modified
files_corrupted = False
for recipe_name in data:
    recipe = data[recipe_name]
    try:
        recipe_content = f"{recipe_name}{recipe['ingredients']}{recipe['instructions']}{recipe['effects']}{recipe['notes']}".encode()
        if hashlib.sha512(recipe_content).hexdigest() != recipe["id"]:
            print(f"Recipe '{recipe_name}' has been modified or is corrupted. ID: {recipe['id']}, Expected: {hashlib.sha512(recipe_content).hexdigest()}")
            files_corrupted = True
    except Exception:
        continue

root = Tk()
icon = PhotoImage(file="assets/img/icon.png")
root.iconphoto(True, icon)
root.geometry("600x400")
root.title("Schedule I DB")

title = Label(root, text="Schedule I DB", font=("Cascadia Code", 24, "underline"))
version_label = Label(root, text="ver1.6.0", font=("Arial", 10))
recipe_list_btn = Button(root, text="Recipe List", font=("Arial", 16), width=20, height=2)
create_recipe_btn = Button(root, text="Create Recipe", font=("Arial", 16), width=20, height=2)
customer_list_btn = Button(root, text="Customer List", font=("Arial", 16), width=20, height=2)

title.pack()
version_label.pack()

if files_corrupted:
    corrupted_label = Label(root, text="WARNING: Some recipes might be corrupted or have been modified without authorization.\nPlease download the newest version of the database.\nIf the problem persists, please contact the developer.\n(check console for more information)", fg="red" , font=("Arial", 10, "bold"))
    corrupted_label.pack()

recipe_list_btn.pack(pady=10)
create_recipe_btn.pack(pady=10)
customer_list_btn.pack(pady=10)
# Bind buttons to their respective functions
recipe_list_btn.config(command=lambda: show_recipe_list_window(root))
create_recipe_btn.config(command=lambda: show_create_recipe_window(root))
customer_list_btn.config(command=lambda: show_customer_list_window(root))




root.mainloop()