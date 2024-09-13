cookbook= {
    "Sandwich": {"ingredients" : ["ham", "bread", "cheese", "tomato"],
                 "meal": "lunch",
                 "prep_time": 10
                },
    "Cake": {"ingredients" : ["flour", "sugar", "eggs"],
             "meal": "dessert",
             "prep_time": 60
            },
    "Salad": {"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
              "meal": "lunch",
              "prep_time": 15
            }
}

def recipes_names():
    if cookbook:
        print("Available recipes:")
        for key in cookbook.keys():
            print(f"- {key}")
    else:
        print("No recipes available.")

def details(name_of_recipe: str):
    recipe = cookbook.get(name_of_recipe)
    if recipe:
        print(f"\nRecipe for {name_of_recipe}:")
        print(f"Ingredients : {', '.join(recipe['ingredients'])}")
        print(f"Meal : {recipe['meal']}")
        print(f"Preparation time : {recipe['prep_time']} minutes")
    else:
        print(f"\nThe recipe for {name_of_recipe} does not exist.")

def delete_recipe(name_of_recipe: str):
    if name_of_recipe in cookbook:
        cookbook.pop(name_of_recipe)
        print(f"Deleted the recipe for {name_of_recipe}.")
    else:
        print(f"\nThe recipe for {name_of_recipe} does not exist.")

def add_recipe():
    name = input("Enter the name of the recipe:\n")

    if name in cookbook:
        print(f"\nA recipe for {name} already exists!")
        return

    ingredients = []
    print("Enter ingredients (press Enter with no input to stop):")
    while True:
        ingredient = input("Ingredient: ")
        if ingredient:
            ingredients.append(ingredient)
        else:
            break

    meal_type = input("Enter the meal type (e.g., lunch, dessert):\n")

    while True:
        try:
            prep_time = int(input("How long will this recipe take (in minutes)?\n"))
            break
        except ValueError:
            print("Please enter a valid number for preparation time.\n")

    cookbook[name] = {
        "ingredients" : ingredients,
        "meal" : meal_type,
        "prep_time" : prep_time
    }

    print(f"\nRecipe for {name} added successfully!")

def main():
    print(
"""
Welcome to the Python Cookbook!

List of available options:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
"""
    )
    while True:
        while True:
            try:
                choice = int(input("\nPlease select an option (1-5):\n>>> "))
                if choice in range(1, 6):
                    break
                else:
                    print("Please select a valid option between 1 and 5.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")

        if choice == 1:
            print("\n")
            add_recipe()
        elif choice == 2:
            print("\n")
            delete_recipe(input("Enter the recipe you would like to delete:\n"))
        elif choice == 3:
            print("\n")
            details(input("Enter the recipe you would like to print:\n"))
        elif choice == 4:
            print("\n")
            recipes_names()
        elif choice == 5:
            print("\nCookbook closed. Goodbye!")
            break

if __name__ == "__main__":
    main()
