import json

print("Recipe Manager\n")

# Global list to hold all recipes
recipes = []

# Defs
def add():
    global recipes
    name = input("Enter the name of the dish: ")
    ingredients = []
    
    # Get ingredients
    while True:
        try:
            ingredientsno = int(input("Enter the number of ingredients: "))
            if ingredientsno <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    for _ in range(ingredientsno):
        ingredient = input("Enter ingredient: ")
        ingredients.append(ingredient)
    
    steps = []
    
    # Get steps
    while True:
        try:
            stepsno = int(input("Enter the number of steps: "))
            if stepsno <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    for _ in range(stepsno):
        step = input("Enter step: ")
        steps.append(step)
    
    # Add recipe to the list
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "steps": steps
    }
    recipes.append(recipe)
    print(f"Recipe for {name} added successfully!")

def delete():
    global recipes
    x = input("Enter name of dish to delete: ")
    for recipe in recipes:
        if recipe["name"].lower() == x.lower():  # Case insensitive match
            recipes.remove(recipe)
            print("Recipe deleted!")
            return
    print("Recipe not found!")

def save():
    with open("recipes.json", "w") as file:
        json.dump(recipes, file)
    print("Recipes saved!")

def load():
    global recipes
    try:
        with open("recipes.json", "r") as file:
            recipes = json.load(file)
        print("Recipes loaded!")
    except FileNotFoundError:
        print("No saved recipes found.")
    except json.JSONDecodeError:
        print("Error loading recipes. The file may be corrupted.")

def view():
    if not recipes:
        print("No recipes available.")
        return
    for idx, recipe in enumerate(recipes, start=1):
        print(f"\nRecipe {idx}: {recipe['name']}")
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(f"- {ingredient}")
        print("Steps:")
        for step in recipe['steps']:
            print(f"- {step}")

while True:
    choice = input("Enter one of the choices by entering numbers:\n1. Add Recipe\n2. Delete Recipe\n3. Save Recipe\n4. Load Recipe\n5. View\n6. Exit\n>> ")
    
    if choice == "1":
        add()
    elif choice == "2":
        delete()
    elif choice == "3":
        save()
    elif choice == "4":
        load()
    elif choice == "5":
        view()
    elif choice == "6":
        break