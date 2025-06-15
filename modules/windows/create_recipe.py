from tkinter import *
from modules.helpers import save_recipe

def show_create_recipe_window(root):
    recipe_window = Toplevel(root)
    recipe_window.title("Create Recipe")
    recipe_window.geometry("900x500")

    # Name section
    name_frame = Frame(recipe_window)
    name_frame.pack(fill=X, padx=10, pady=5)
    name_label = Label(name_frame, text="Recipe Name")
    name_label.pack()
    name_entry = Entry(name_frame)
    name_entry.pack(fill=X)

    # Create main content frame for two columns
    content_frame = Frame(recipe_window)
    content_frame.pack(fill=BOTH, expand=True, padx=10)

    # Left column
    left_frame = Frame(content_frame)
    left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
    
    ingredients_label = Label(left_frame, text="Ingredients")
    ingredients_label.pack()
    ingredients_entry = Text(left_frame, height=10, width=40)
    ingredients_entry.pack(fill=BOTH, expand=True)

    instructions_label = Label(left_frame, text="Instructions")
    instructions_label.pack()
    instructions_entry = Text(left_frame, height=10, width=40)
    instructions_entry.pack(fill=BOTH, expand=True)

    # Right column
    right_frame = Frame(content_frame)
    right_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

    effects_label = Label(right_frame, text="Effects")
    effects_label.pack()
    effects_entry = Text(right_frame, height=10, width=20)
    effects_entry.pack(fill=BOTH, expand=True)

    notes_label = Label(right_frame, text="Notes")
    notes_label.pack()
    notes_entry = Text(right_frame, height=10, width=20)
    notes_entry.pack(fill=BOTH, expand=True)

    def save_and_close():
        name = name_entry.get()
        ingredients = ingredients_entry.get("1.0", END)
        instructions = instructions_entry.get("1.0", END)
        effects = effects_entry.get("1.0", END)
        notes = notes_entry.get("1.0", END)
        save_recipe(name, ingredients, instructions, effects, notes)
        recipe_window.destroy()

    # Save button at bottom
    save_button = Button(recipe_window, text="Save Recipe", command=save_and_close)
    save_button.pack(pady=10)