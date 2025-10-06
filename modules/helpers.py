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
    "Schizophrenia",
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

class ProductAffinity:
    def __init__(self, weed, meth, cocaine):
        self.weed = weed
        self.meth = meth
        self.cocaine = cocaine

    def get_highest_affinity(self):
        """Return the product type (string) with the highest affinity number"""
        affinities = {
            'weed': self.weed,
            'meth': self.meth,
            'cocaine': self.cocaine
        }
        return max(affinities.items(), key=lambda x: x[1])[0]
    
class Customer:
    def __init__(self, name: str, area: str, standards: str, product_affinity: ProductAffinity, min_spend: int, max_spend: int):
        if not name or not area or not standards or not isinstance(product_affinity, ProductAffinity) or not min_spend or not max_spend:
            raise ValueError("All fields must be provided with a valid value.")
        if min_spend < 0 or max_spend < 0 or min_spend > max_spend:
            raise ValueError("Minimum spend must be less than or equal to maximum spend and both must be non-negative.")
        
        self.name = name
        self.area = area
        self.standards = standards
        self.product_affinity = product_affinity
        self.min_spend = min_spend
        self.max_spend = max_spend
        self.img = f"assets/img/customers/{self.name.lower().replace(" ", "_")}.png"

customers = [
        Customer("Alison Knight", "Suburbia", "High", ProductAffinity(-0.63, 0.27, 1.00), 800, 1200),
        Customer("Anna Chesterfield", "Docks", "Moderate", ProductAffinity(1.00, -0.86, 0.51), 600, 1000),
        Customer("Austin Steiner", "Northtown", "Low", ProductAffinity(0.78, -0.66, 0.15), 400, 800),
        Customer("Beth Penn", "Northtown", "Low", ProductAffinity(0.30, 0.31, -0.20), 200, 500),
        Customer("Billy Kramer", "Docks", "Moderate", ProductAffinity(0.08, -0.63, 0.50), 600, 1000),
        Customer("Carl Bundy", "Suburbia", "High", ProductAffinity(-0.81, -0.23, -0.58), 800, 1200),
        Customer("Charles Rowland", "Westville", "Low", ProductAffinity(0.55, 0.24, 1.00), 400, 800),
        Customer("Chloe Bowers", "Northtown", "Low", ProductAffinity(0.44, 0.79, 0.25), 200, 500),
        Customer("Chris Sullivan", "Suburbia", "High", ProductAffinity(-0.83, 0.40, 0.79), 800, 1200),
        Customer("Cranky Frank", "Docks", "Moderate", ProductAffinity(0.68, 1.00, 0.02), 600, 1000),
        Customer("Dean Webster", "Westville", "Low", ProductAffinity(0.51, 1.00, 0.00), 500, 1200),
        Customer("Dennis Kennedy", "Suburbia", "High", ProductAffinity(0.26, 0.08, -0.89), 800, 1200),
        Customer("Donna Martin", "Northtown", "Low", ProductAffinity(0.93, -0.27, 0.25), 200, 500),
        Customer("Doris Lubbin", "Westville", "Low", ProductAffinity(0.46, 0.16, 0.58), 200, 500),
        Customer("Elizabeth Homley", "Downtown", "Moderate", ProductAffinity(0.33, 0.45, 0.32), 400, 800),
        Customer("Eugene Buckley", "Downtown", "Moderate", ProductAffinity(0.66, 0.11, 0.17), 400, 800),
        Customer("Fiona Hancock", "Uptown", "High", ProductAffinity(0.03, 0.08, -0.50), 1000, 2000),
        Customer("Genghis Barn", "Docks", "Very Low", ProductAffinity(0.85, -0.64, 0.45), 600, 1000),
        Customer("George Greene", "Westville", "Low", ProductAffinity(0.90, 0.37, -0.15), 500, 1400),
        Customer("Geraldine Poon", "Northtown", "Very Low", ProductAffinity(1.00, 0.66, 0.26), 600, 1200),
        Customer("Greg Figgle", "Downtown", "Very Low", ProductAffinity(0.58, -0.58, -0.35), 400, 800),
        Customer("Hank Stevenson", "Suburbia", "High", ProductAffinity(-0.58, 0.56, 0.21), 800, 1200),
        Customer("Harold Colt", "Suburbia", "High", ProductAffinity(-0.95, -0.78, -0.70), 800, 1200),
        Customer("Herbert Bleuball", "Uptown", "High", ProductAffinity(0.81, 0.39, 0.27), 1000, 2000),
        Customer("Jack Knight", "Suburbia", "High", ProductAffinity(0.66, 0.89, 0.10), 800, 1200),
        Customer("Jackie Stevenson", "Suburbia", "High", ProductAffinity(0.89, -0.60, 0.28), 800, 1200),
        Customer("Javier Perez", "Docks", "Moderate", ProductAffinity(0.72, -0.30, 0.45), 600, 1000),
        Customer("Jeff Gilmore", "Downtown", "Moderate", ProductAffinity(0.75, -0.84, -0.31), 400, 800),
        Customer("Jen Heard", "Uptown", "High", ProductAffinity(0.41, -0.79, 1.00), 1000, 2000),
        Customer("Jennifer Rivera", "Downtown", "Moderate", ProductAffinity(-0.88, 0.42, 0.65), 400, 800),
        Customer("Jeremy Wilkinson", "Suburbia", "High", ProductAffinity(0.58, 0.53, 0.83), 800, 1200),
        Customer("Jerry Montero", "Westville", "Low", ProductAffinity(0.34, 0.00, 0.61), 500, 1000),
        Customer("Jessi Waters", "Northtown", "Very Low", ProductAffinity(0.00, 1.00, -0.27), 200, 1200),
        Customer("Joyce Ball", "Westville", "Low", ProductAffinity(1.00, 0.59, -0.64), 200, 500),
        Customer("Karen Kennedy", "Suburbia", "High", ProductAffinity(0.53, -0.51, 0.55), 800, 1200),
        Customer("Kathy Henderson", "Northtown", "Low", ProductAffinity(0.55, 0.27, -0.61), 400, 800),
        Customer("Keith Wagner", "Westville", "Very Low", ProductAffinity(0.00, 1.00, 0.21), 200, 500),
        Customer("Kevin Oakley", "Downtown", "Moderate", ProductAffinity(0.72, -0.51, 0.62), 400, 800),
        Customer("Kim Delaney", "Westville", "Low", ProductAffinity(0.73, -0.57, 0.86), 400, 800),
        Customer("Kyle Cooley", "Northtown", "Low", ProductAffinity(0.72, 0.70, -0.41), 400, 900),
        Customer("Lily Turner", "Uptown", "High", ProductAffinity(0.32, -0.40, 0.84), 1000, 2000),
        Customer("Lisa Gardener", "Docks", "Moderate", ProductAffinity(-0.82, -0.36, -0.28), 600, 1000),
        Customer("Louis Fourier", "Downtown", "Moderate", ProductAffinity(0.94, -0.92, -0.30), 400, 800),
        Customer("Lucy Pennington", "Downtown", "Moderate", ProductAffinity(0.64, -0.80, 0.19), 400, 800),
        Customer("Ludwig Meyer", "Northtown", "Low", ProductAffinity(0.79, -0.59, -0.68), 200, 500),
        Customer("Mac Cooper", "Docks", "Moderate", ProductAffinity(-0.57, -0.38, 0.27), 600, 1000),
        Customer("Marco Barone", "Docks", "Moderate", ProductAffinity(0.34, 0.08, 0.54), 600, 1000),
        Customer("Meg Cooley", "Westville", "Low", ProductAffinity(0.79, -0.04, 0.72), 200, 500),
        Customer("Melissa Wood", "Docks", "Moderate", ProductAffinity(-0.26, 0.67, 0.42), 600, 1000),
        Customer("Michael Boog", "Uptown", "High", ProductAffinity(0.17, 0.95, 0.70), 1000, 2000),
        Customer("Mick Lubbin", "Northtown", "Low", ProductAffinity(-0.73, 0.88, 0.37), 400, 800),
        Customer("Mrs. Ming", "Northtown", "Low", ProductAffinity(0.61, -0.25, -0.22), 200, 500),
        Customer("Pearl Moore", "Uptown", "High", ProductAffinity(0.89, -0.89, 0.67), 1000, 2000),
        Customer("Peggy Myers", "Northtown", "Low", ProductAffinity(0.23, -0.64, 1.00), 400, 800),
        Customer("Peter File", "Northtown", "Low", ProductAffinity(1.00, 0.40, 0.74), 400, 800),
        Customer("Philip Wentworth", "Downtown", "Moderate", ProductAffinity(0.97, 0.78, -0.22), 400, 800),
        Customer("Randy Caulfield", "Downtown", "Moderate", ProductAffinity(1.00, -0.28, -0.47), 400, 800),
        Customer("Ray Hoffman", "Uptown", "High", ProductAffinity(0.56, 0.00, 1.00), 1000, 2000),
        Customer("Sam Thompson", "Northtown", "Low", ProductAffinity(-0.76, 0.30, -0.80), 200, 500),
        Customer("Tobas Wentworth", "Uptown", "High", ProductAffinity(0.19, 0.76, 0.17), 1000, 2000),
        Customer("Trent Sherman", "Westville", "Low", ProductAffinity(0.68, 0.23, 0.90), 200, 500),
        Customer("Walter Cussler", "Uptown", "High", ProductAffinity(-0.14, -0.30, -0.44), 1000, 2000),]