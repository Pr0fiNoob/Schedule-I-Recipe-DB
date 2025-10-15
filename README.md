# Schedule I DB

A database for recipes and other stuff in Schedule I. Schedule I is a game, this is **NOT** a database for actual drugs! (Please don't do drugs.)

## Features

- **Recipe Management:**  
  Add, edit, delete, and view recipes with details such as ingredients, instructions, effects, and additional notes.

- **Customer Management:**  
  View a scrollable, detailed list of customers, including their preferences, area, standards, and spend range.

- **Search and Filter:**  
  Quickly search for recipes by name and filter them by effects using a multi-select filter.

- **Data Integrity:**  
  Ensures the integrity of the database by verifying recipe hashes to detect unauthorized modifications.


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

5. **View Customer Data**:
   - Click on the "Customer List" button to view a list of all customers and their data.


## Requirements

- Python 3.7 or higher
- Required libraries: `tkinter`, `hashlib`, `json`


## Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests for new features, bug fixes, improvements or new recipes for the database (just please check that your recipe doesn't already exist in the database).


## Disclaimer

This project is for educational and entertainment purposes only.  
All recipes and customer data are fictional and part of the game "Schedule I" made by TVGS (Tylers Video Game Studio).

## Sources
- Recipe Data has been collected by contributors either by trial and error or using [Schedule I Calculator](schedule1-calculator.com)
- Customer Data is entirely from [Schedule I Wiki](schedule-1.fandom.com/wiki/Customers)


## License

This project is licensed under the [MIT License](LICENSE).
