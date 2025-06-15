from tkinter import *
from tkinter import messagebox
from edit_recipe import show_edit_recipe_window
from helpers import EFFECTS, format_effects, save_recipe
import json

def show_recipe_list_window(root):
    with open("db.json", "r") as file:
        data = json.load(file)

    selected_effects = []

    def search_recipes(*args):
        search_query = search_entry.get().lower()
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        for recipe_name, recipe in data.items():
            name_matches = search_query in recipe_name.lower()
            recipe_effects = [effect.lower() for effect in recipe.get("effects", "").split("\n") if effect]
            effect_matches = (
                not selected_effects or
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

        top_frame = Frame(recipe_frame)
        top_frame.pack(fill=X, padx=5, pady=5)

        recipe_label = Label(top_frame, text=recipe_name, font=("Arial", 12, "bold"))
        recipe_label.pack(side=LEFT)

        buttons_frame = Frame(top_frame)
        buttons_frame.pack(side=RIGHT)

        edit_button = Button(buttons_frame, text="Edit", command=lambda: show_edit_recipe_window(root, recipe_name))
        edit_button.pack(side=LEFT, padx=2)

        def delete_recipe():
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{recipe_name}'?"):
                del data[recipe_name]
                with open("db.json", "w") as file:
                    json.dump(data, file, indent=4)
                recipe_frame.destroy()
                messagebox.showinfo("Deleted successfully", f"Recipe '{recipe_name}' has been deleted.")

        delete_button = Button(buttons_frame, text="Delete", command=delete_recipe)
        delete_button.pack(side=LEFT, padx=2)

        content_frame = Frame(recipe_frame)
        content_frame.pack(fill=BOTH, expand=True, padx=5)

        left_frame = Frame(content_frame)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

        right_frame = Frame(content_frame)
        right_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

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

    search_frame = Frame(recipe_window)
    search_frame.pack(fill=X, padx=10, pady=5)
    
    search_label = Label(search_frame, text="Search:", font=("Arial", 10))
    search_label.pack(side=LEFT, padx=5)
    
    search_entry = Entry(search_frame, font=("Arial", 10))
    search_entry.pack(side=LEFT, fill=X, expand=True, padx=5)
    
    # You can add effect filter button here if you want

    search_entry.bind('<KeyRelease>', search_recipes)

    canvas = Canvas(recipe_window)
    scrollbar = Scrollbar(recipe_window, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    for recipe_name, recipe in data.items():
        add_recipe_to_frame(recipe_name, recipe)