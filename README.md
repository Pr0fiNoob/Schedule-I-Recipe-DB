# Schedule I Recipe DB

A database for all recipes and mixtures in Schedule I. Schedule I is a game, this is **NOT** a database for actual drugs! (Please don't do drugs.)

## Features

- **Recipe Management**: Add, edit, delete, and view recipes with detailed information such as ingredients, instructions, effects, and notes.
- **Search and Filter**: Quickly search for recipes by name or filter them based on specific effects.
- **Data Integrity**: Ensures the integrity of the database by verifying recipe hashes to detect unauthorized modifications.
- **User-Friendly Interface**: Built with a graphical user interface (GUI) using Python's `tkinter` library.

## How to Use

1. **Launch the Application**:
   - Run the `launcher.cmd` file or execute `python main.py` in your terminal.

2. **View Recipes**:
   - Click on the "Recipe List" button to view all available recipes.
   - Use the search bar to find recipes by name or filter them by effects.

3. **Create a New Recipe**:
   - Click on the "Create Recipe" button to add a new recipe.
   - Fill in the recipe details (name, ingredients, instructions, effects, and notes) and click "Save Recipe."

4. **Edit or Delete Recipes**:
   - In the recipe list, click "Edit" to modify a recipe or "Delete" to remove it from the database.


## Requirements

- Python 3.7 or higher
- Required libraries: `tkinter`, `hashlib`, `json`

