import hashlib
import json


def format_effects(effects_text):
    """Standardize effects format: lowercase with first letter capitalized"""
    if not effects_text:
        return ""
    effects = [e.strip() for e in effects_text.split('\n') if e.strip()]
    return '\n'.join(e[0].upper() + e[1:].lower() if e else '' for e in effects)


def save_recipe(name, ingredients, instructions, effects, notes):
    if not name or not ingredients or not instructions:
        return

    # Format effects before saving
    formatted_effects = format_effects(effects)

    # Combine all recipe content for hashing
    recipe_content = f"{name.strip()}{ingredients.strip()}{instructions.strip()}{formatted_effects.strip()}{notes.strip()}".encode()
    recipe_id = hashlib.sha512(recipe_content).hexdigest()

    # Load data
    with open("db.json", "r") as file:
        data = json.load(file)

    recipe = {
        "ingredients": ingredients.strip(),
        "instructions": instructions.strip(),
        "effects": formatted_effects,
        "notes": notes.strip(),
        "id": recipe_id
    }

    data[f"{name}"] = recipe
    with open("db.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Recipe '{name}' saved with ID: {recipe_id}")

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