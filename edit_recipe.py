from tkinter import *
import json
from helpers import save_recipe

def show_edit_recipe_window(root, recipe_name):
    with open("db.json", "r") as file:
        data = json.load(file)
    recipe = data[recipe_name]

    edit_window = Toplevel(root)
    edit_window.title(f"Edit Recipe - {recipe_name}")
    edit_window.geometry("900x500")

    # Create main content frame for two columns
    content_frame = Frame(edit_window)
    content_frame.pack(fill=BOTH, expand=True, padx=10)

    # Left column
    left_frame = Frame(content_frame)
    left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
    
    ingredients_label = Label(left_frame, text="Ingredients")
    ingredients_label.pack()
    ingredients_entry = Text(left_frame, height=10, width=40)
    ingredients_entry.insert(END, recipe["ingredients"])
    ingredients_entry.pack(fill=BOTH, expand=True)

    instructions_label = Label(left_frame, text="Instructions")
    instructions_label.pack()
    instructions_entry = Text(left_frame, height=10, width=40)
    instructions_entry.insert(END, recipe["instructions"])
    instructions_entry.pack(fill=BOTH, expand=True)

    # Right column
    right_frame = Frame(content_frame)
    right_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

    effects_label = Label(right_frame, text="Effects")
    effects_label.pack()
    effects_entry = Text(right_frame, height=10, width=20)
    effects_entry.insert(END, recipe.get("effects", ""))
    effects_entry.pack(fill=BOTH, expand=True)

    notes_label = Label(right_frame, text="Notes")
    notes_label.pack()
    notes_entry = Text(right_frame, height=10, width=20)
    notes_entry.insert(END, recipe.get("notes", ""))
    notes_entry.pack(fill=BOTH, expand=True)

    def save_and_close():
        ingredients = ingredients_entry.get("1.0", END)
        instructions = instructions_entry.get("1.0", END)
        effects = effects_entry.get("1.0", END)
        notes = notes_entry.get("1.0", END)
        save_recipe(recipe_name, ingredients, instructions, effects, notes)
        edit_window.destroy()

    # Save button at bottom
    save_button = Button(edit_window, text="Save Changes", command=save_and_close)
    save_button.pack(pady=10)