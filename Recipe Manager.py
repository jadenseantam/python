import json
import os
from tkinter import Tk, filedialog

print("Recipe Manager\n")

# Global list to hold all recipes
recipes = []

# Function to open a file dialog and select an image
def select_image():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select an image",
                                            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    root.destroy()  # Close the file dialog
    return file_path

# Defs
def add():
    global recipes
    name = input("Enter the name of the dish: ")
    ingredients = []

    # Get ingredients
    while True:
        ingredient = input("Enter the ingredient, \"n\" to finish: ")
        if ingredient.lower() == "n":
            break
        ingredients.append(ingredient)

    steps = []

    # Get steps
    while True:
        step = input("Enter a step, or \"n\" to finish: ")
        if step.lower() == "n":
            break
        image_path = select_image()
        steps.append({
            "step": step,
            "image": image_path if image_path else None
        })

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
    name = input("Enter the name of the recipe to load: ")
    try:
        with open("recipes.json", "r") as file:
            all_recipes = json.load(file)
            for recipe in all_recipes:
                if recipe["name"].lower() == name.lower():
                    recipes.append(recipe)
                    print(f"Recipe '{name}' loaded successfully!")
                    return
            print("Recipe not found.")
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
            print(f"- {step['step']}")
            if step['image']:
                print(f"  Image: {os.path.basename(step['image'])}")

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
    else:
        print("Invalid input. Please try again.\n")