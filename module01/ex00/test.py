# test.py

from book import Book
from recipe import Recipe

# Test cases for Recipe class
def test_recipe_class():
    print("Testing Recipe class...\n")

    # Valid Recipe instance
    try:
        pancake = Recipe(
            name="Pancake",
            cooking_lvl=2,
            cooking_time=15,
            ingredients=["flour", "milk", "eggs"],
            description="A simple pancake recipe.",
            recipe_type="dessert"
        )
        print(f"Created recipe: {pancake.name}")
        print(pancake)
    except Exception as e:
        print("Failed to create a valid Recipe instance:", e)

    # Invalid cooking_lvl (out of range)
    try:
        invalid_recipe = Recipe(
            name="InvalidLevel",
            cooking_lvl=6,  # Invalid level
            cooking_time=10,
            ingredients=["ingredient1"],
            description="Invalid cooking level.",
            recipe_type="starter"
        )
    except ValueError as e:
        print("Correctly caught an error for invalid cooking_lvl:", e)

    # Invalid cooking_time (negative)
    try:
        invalid_recipe = Recipe(
            name="NegativeTime",
            cooking_lvl=3,
            cooking_time=-5,  # Negative time
            ingredients=["ingredient1"],
            description="Negative cooking time.",
            recipe_type="starter"
        )
    except ValueError as e:
        print("Correctly caught an error for negative cooking_time:", e)

    # Invalid ingredients (not a list)
    try:
        invalid_recipe = Recipe(
            name="InvalidIngredients",
            cooking_lvl=3,
            cooking_time=10,
            ingredients="ingredient1",  # Should be a list
            description="Ingredients not a list.",
            recipe_type="starter"
        )
    except TypeError as e:
        print("Correctly caught an error for invalid ingredients:", e)

    # Invalid recipe_type
    try:
        invalid_recipe = Recipe(
            name="InvalidType",
            cooking_lvl=3,
            cooking_time=10,
            ingredients=["ingredient1"],
            description="Invalid recipe type.",
            recipe_type="snack"  # Invalid type
        )
    except ValueError as e:
        print("Correctly caught an error for invalid recipe_type:", e)

    print("\nRecipe class tests completed.\n")

# Test cases for Book class
def test_book_class():
    print("Testing Book class...\n")

    # Create a Book instance
    try:
        my_cookbook = Book("My Cookbook")
        print(f"Created Book: {my_cookbook.name}")
        print(f"Creation Date: {my_cookbook.creation_date}")
        print(f"Last Update: {my_cookbook.last_update}")
    except Exception as e:
        print("Failed to create a Book instance:", e)

    # Create Recipe instances
    salad = Recipe(
        name="Salad",
        cooking_lvl=1,
        cooking_time=5,
        ingredients=["lettuce", "tomato", "cucumber"],
        description="A fresh salad.",
        recipe_type="starter"
    )

    steak = Recipe(
        name="Steak",
        cooking_lvl=4,
        cooking_time=30,
        ingredients=["beef", "salt", "pepper"],
        description="Grilled steak.",
        recipe_type="lunch"
    )

    ice_cream = Recipe(
        name="Ice Cream",
        cooking_lvl=2,
        cooking_time=120,
        ingredients=["milk", "sugar", "vanilla"],
        description="Homemade ice cream.",
        recipe_type="dessert"
    )

    # Add recipes to the book
    print("\nAdding recipes to the book...")
    my_cookbook.add_recipe(pancake)  # From previous function
    my_cookbook.add_recipe(salad)
    my_cookbook.add_recipe(steak)
    my_cookbook.add_recipe(ice_cream)
    print(f"Last Update after adding recipes: {my_cookbook.last_update}")

    # Test get_recipe_by_name
    print("\nTesting get_recipe_by_name:")
    found_recipe = my_cookbook.get_recipe_by_name("Pancake")
    if found_recipe:
        print(found_recipe)

    found_recipe = my_cookbook.get_recipe_by_name("Steak")
    if found_recipe:
        print(found_recipe)

    found_recipe = my_cookbook.get_recipe_by_name("Nonexistent")  # Should inform not found

    # Test get_recipes_by_types
    print("\nTesting get_recipes_by_types:")
    starters = my_cookbook.get_recipes_by_types("starter")
    print("Starters:", starters)

    lunches = my_cookbook.get_recipes_by_types("lunch")
    print("Lunches:", lunches)

    desserts = my_cookbook.get_recipes_by_types("dessert")
    print("Desserts:", desserts)

    # Test invalid recipe type
    invalid_recipes = my_cookbook.get_recipes_by_types("snack")
    print("Invalid recipe type retrieval:", invalid_recipes)

    # Test adding invalid recipe
    print("\nTesting adding invalid recipe:")
    try:
        my_cookbook.add_recipe("Not a recipe instance")  # Should raise error
    except TypeError as e:
        print("Correctly caught an error when adding invalid recipe:", e)

    print("\nBook class tests completed.\n")

# Run tests
if __name__ == "__main__":
    # Test Recipe class
    test_recipe_class()

    # Need to create pancake instance again for Book tests
    pancake = Recipe(
        name="Pancake",
        cooking_lvl=2,
        cooking_time=15,
        ingredients=["flour", "milk", "eggs"],
        description="A simple pancake recipe.",
        recipe_type="dessert"
    )

    # Test Book class
    test_book_class()
