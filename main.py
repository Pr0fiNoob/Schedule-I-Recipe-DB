from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Add this import for Combobox
import hashlib
import json

# Add this helper function after the imports
def format_effects(effects_text):
    """Standardize effects format: lowercase with first letter capitalized"""
    if not effects_text:
        return ""
    effects = [e.strip() for e in effects_text.split('\n') if e.strip()]
    return '\n'.join(e[0].upper() + e[1:].lower() if e else '' for e in effects)

# Predefined effects (add your effects here)
EFFECTS = [
    "Anti-Gravity",
    "Athletic",
    "Balding",
    "Bright-Eyed",
    "Calming",
    "Calorie-Dense",
    "Cyclopean",
    "Disorienting",
    "Electrifying",
    "Energizing",
    "Euphoric",
    "Explosive",
    "Focused",
    "Foggy",
    "Gingeritis",
    "Glowing",
    "Jennerising",
    "Laxative",
    "Long Faced",
    "Munchies",
    "Paranoia",
    "Refreshing",
    "schizophrenia",
    "Sedating",
    "Seizure-Inducing",
    "Shrinking",
    "Slippery",
    "Smelly",
    "Sneaky",
    "Spicy",
    "Thought-Provoking",
    "Toxic",
    "Tropic Thunder",
    "Zombifying"
]

# Open Database
with open("db.json", "r") as file:
    data = json.load(file)
    file.close()

# Check if the database is corrupted or modified
files_corrupted = False
for recipe_name in data:
    recipe = data[recipe_name]
    recipe_content = f"{recipe_name}{recipe['ingredients']}{recipe['instructions']}{recipe['effects']}{recipe['notes']}".encode()
    if hashlib.sha512(recipe_content).hexdigest() != recipe["id"]:
        print(f"Recipe '{recipe_name}' has been modified or is corrupted. ID: {recipe['id']}, Expected: {hashlib.sha512(recipe_content).hexdigest()}")
        files_corrupted = True

def edit_recipe(recipe_name):
    def save_and_close():
        ingredients = ingredients_entry.get("1.0", END)
        instructions = instructions_entry.get("1.0", END)
        effects = effects_entry.get("1.0", END)
        notes = notes_entry.get("1.0", END)
        save_recipe(recipe_name, ingredients, instructions, effects, notes)
        edit_window.destroy()

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
    ingredients_entry.insert(END, data[recipe_name]["ingredients"])
    ingredients_entry.pack(fill=BOTH, expand=True)

    instructions_label = Label(left_frame, text="Instructions")
    instructions_label.pack()
    instructions_entry = Text(left_frame, height=10, width=40)
    instructions_entry.insert(END, data[recipe_name]["instructions"])
    instructions_entry.pack(fill=BOTH, expand=True)

    # Right column
    right_frame = Frame(content_frame)
    right_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

    effects_label = Label(right_frame, text="Effects")
    effects_label.pack()
    effects_entry = Text(right_frame, height=10, width=20)
    effects_entry.insert(END, data[recipe_name].get("effects", ""))
    effects_entry.pack(fill=BOTH, expand=True)

    notes_label = Label(right_frame, text="Notes")
    notes_label.pack()
    notes_entry = Text(right_frame, height=10, width=20)
    notes_entry.insert(END, data[recipe_name].get("notes", ""))
    notes_entry.pack(fill=BOTH, expand=True)

    # Save button at bottom
    save_button = Button(edit_window, text="Save Changes", command=save_and_close)
    save_button.pack(pady=10)

def delete_recipe(recipe_name, recipe_frame):
    from tkinter import messagebox
    if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{recipe_name}'?"):
        del data[recipe_name]
        with open("db.json", "w") as file:
            json.dump(data, file, indent=4)
        recipe_frame.destroy()
        messagebox.showinfo("Deleted successfully", f"Recipe '{recipe_name}' has been deleted.")

def show_recipe_list():
    # read database again to ensure we have the latest version
    with open("db.json", "r") as file:
        data = json.load(file)
        file.close()

    # Keep track of currently selected effects
    selected_effects = []

    def search_recipes(*args):
        search_query = search_entry.get().lower()
        
        # Clear current recipes
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        
        # Add matching recipes
        for recipe_name, recipe in data.items():
            name_matches = search_query in recipe_name.lower()
            
            # Get recipe effects and convert to lowercase
            recipe_effects = [effect.lower() for effect in recipe.get("effects", "").split("\n") if effect]
            
            # Check if ALL selected effects are in recipe effects
            effect_matches = (
                not selected_effects or  # No effects selected, show all
                all(effect.lower() in recipe_effects for effect in selected_effects)
            )
            
            if name_matches and effect_matches:
                add_recipe_to_frame(recipe_name, recipe)

    def update_selected_effects(effects):
        nonlocal selected_effects
        selected_effects = effects
        search_recipes()

    def add_recipe_to_frame(recipe_name, recipe):
        recipe_frame = Frame(scrollable_frame, borderwidth=2, relief="solid", padx=5, pady=5)
        recipe_frame.pack(pady=5, fill=X, expand=True)

        # Top row with recipe name and buttons
        top_frame = Frame(recipe_frame)
        top_frame.pack(fill=X, padx=5, pady=5)

        recipe_label = Label(top_frame, text=recipe_name, font=("Arial", 12, "bold"))
        recipe_label.pack(side=LEFT)

        # Add buttons frame
        buttons_frame = Frame(top_frame)
        buttons_frame.pack(side=RIGHT)

        edit_button = Button(buttons_frame, text="Edit", command=lambda: edit_recipe(recipe_name))
        edit_button.pack(side=LEFT, padx=2)

        delete_button = Button(buttons_frame, text="Delete", 
                            command=lambda: delete_recipe(recipe_name, recipe_frame))
        delete_button.pack(side=LEFT, padx=2)

        # Create content frame for two columns
        content_frame = Frame(recipe_frame)
        content_frame.pack(fill=BOTH, expand=True, padx=5)

        # Create left column frame
        left_frame = Frame(content_frame)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

        # Create right column frame
        right_frame = Frame(content_frame)
        right_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

        # Left column - Ingredients and Instructions
        ingredients_label = Label(left_frame, text="Ingredients:", font=("Arial", 10, "italic"))
        ingredients_label.pack(anchor="w")
        ingredients_text = Text(left_frame, height=5, width=40, wrap=WORD)
        ingredients_text.insert(END, recipe["ingredients"])
        ingredients_text.config(state=DISABLED)
        ingredients_text.pack(fill=BOTH)

        instructions_label = Label(left_frame, text="Instructions:", font=("Arial", 10, "italic"))
        instructions_label.pack(anchor="w")
        instructions_text = Text(left_frame, height=5, width=40, wrap=WORD)
        instructions_text.insert(END, recipe["instructions"])
        instructions_text.config(state=DISABLED)
        instructions_text.pack(fill=BOTH)

        # Right column - Effects and Notes
        effects_label = Label(right_frame, text="Effects:", font=("Arial", 10, "italic"))
        effects_label.pack(anchor="w")
        effects_text = Text(right_frame, height=5, width=25, wrap=WORD)
        effects_text.insert(END, recipe.get("effects", ""))
        effects_text.config(state=DISABLED)
        effects_text.pack(fill=BOTH)

        notes_label = Label(right_frame, text="Notes:", font=("Arial", 10, "italic"))
        notes_label.pack(anchor="w")
        notes_text = Text(right_frame, height=5, width=25, wrap=WORD)
        notes_text.insert(END, recipe.get("notes", ""))
        notes_text.config(state=DISABLED)
        notes_text.pack(fill=BOTH)

    recipe_window = Toplevel(root)
    recipe_window.title("Recipe List")
    recipe_window.geometry("600x450")

    # Update search frame code
    search_frame = Frame(recipe_window)
    search_frame.pack(fill=X, padx=10, pady=5)
    
    search_label = Label(search_frame, text="Search:", font=("Arial", 10))
    search_label.pack(side=LEFT, padx=5)
    
    search_entry = Entry(search_frame, font=("Arial", 10))
    search_entry.pack(side=LEFT, fill=X, expand=True, padx=5)
    
    effects_button = Button(search_frame, text="Filter Effects", 
                        command=lambda: show_effects_filter(recipe_window, update_selected_effects))
    effects_button.pack(side=RIGHT, padx=5)
    
    # Bind search event
    search_entry.bind('<KeyRelease>', search_recipes)

    # Create a canvas and a scrollbar
    canvas = Canvas(recipe_window)
    scrollbar = Scrollbar(recipe_window, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = Frame(canvas)

    # Configure the canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Add recipes to the scrollable frame
    for recipe_name, recipe in data.items():
        add_recipe_to_frame(recipe_name, recipe)

def create_recipe():
    def save_and_close():
        name = name_entry.get()
        ingredients = ingredients_entry.get("1.0", END)
        instructions = instructions_entry.get("1.0", END)
        effects = effects_entry.get("1.0", END)
        notes = notes_entry.get("1.0", END)
        save_recipe(name, ingredients, instructions, effects, notes)
        recipe_window.destroy()

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

    # Save button at bottom
    save_button = Button(recipe_window, text="Save Recipe", command=save_and_close)
    save_button.pack(pady=10)

def save_recipe(name, ingredients, instructions, effects, notes):
    if not name or not ingredients or not instructions:
        return

    # Format effects before saving
    formatted_effects = format_effects(effects)

    # Combine all recipe content for hashing
    recipe_content = f"{name.strip()}{ingredients.strip()}{instructions.strip()}{formatted_effects.strip()}{notes.strip()}".encode()
    recipe_id = hashlib.sha512(recipe_content).hexdigest()

    recipe = {
        "ingredients": ingredients.strip(),
        "instructions": instructions.strip(),
        "effects": formatted_effects,  # Store formatted effects
        "notes": notes.strip(),
        "id": recipe_id
    }

    # Save the recipe to a JSON file
    data[f"{name}"] = recipe
    with open("db.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Recipe '{name}' saved with ID: {recipe_id}")

def show_effects_filter(parent, callback):
    filter_window = Toplevel(parent)
    filter_window.title("Filter Effects")
    filter_window.geometry("300x630")

    # Create frame for effects list
    effects_frame = Frame(filter_window)
    effects_frame.pack(fill=BOTH, expand=True, padx=10, pady=5)

    # Label
    Label(effects_frame, text="Select Effects:", font=("Arial", 10, "bold")).pack(pady=5)

    # Create Listbox for multiple effect selection
    effects_list = Listbox(effects_frame, selectmode=MULTIPLE, height=15)
    for effect in EFFECTS:  # Skip "All Effects"
        effects_list.insert(END, effect)
    effects_list.pack(side=LEFT, fill=BOTH, expand=True)

    # Add scrollbar
    scrollbar = Scrollbar(effects_frame, orient=VERTICAL, command=effects_list.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    effects_list.config(yscrollcommand=scrollbar.set)

    # Buttons frame
    button_frame = Frame(filter_window)
    button_frame.pack(fill=X, padx=10, pady=5)

    def select_all():
        effects_list.select_set(0, END)

    def deselect_all():
        effects_list.selection_clear(0, END)

    def apply_filter():
        selected = [effects_list.get(i) for i in effects_list.curselection()]
        callback(selected)
        filter_window.destroy()

    # Add buttons
    Button(button_frame, text="Select All", command=select_all).pack(side=LEFT, padx=5)
    Button(button_frame, text="Deselect All", command=deselect_all).pack(side=LEFT, padx=5)
    Button(button_frame, text="Apply Filter", command=apply_filter).pack(side=RIGHT, padx=5)

root = Tk()

icon = PhotoImage(file="icon.png")
root.iconphoto(True, icon)
root.geometry("600x400")
root.title("Schedule I Recipe DB")


title = Label(root, text="Schedule  Recipe DB", font=("Arial", 24, "underline"))
recipe_list_btn = Button(root, text="Recipe List", font=("Arial", 16), width=20, height=2)
create_recipe_btn = Button(root, text="Create Recipe", font=("Arial", 16), width=20, height=2)

title.pack()

if files_corrupted:
    corrupted_label = Label(root, text="WARNING: Some recipes might be corrupted or have been modified without authorization.\nPlease download the newest version of the database.\nIf the problem persists, please contact the developer.\n(check console for more information)", fg="red" , font=("Arial", 10, "bold"))
    corrupted_label.pack()

recipe_list_btn.pack(pady=10)
create_recipe_btn.pack(pady=10)
recipe_list_btn.config(command=show_recipe_list)
create_recipe_btn.config(command=create_recipe)



root.mainloop()

