# recipe.py
class Recipe:
	def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: str, recipe_type: str) -> None:
		# if not isinstance(name, str) or not name:
		# 	print("Error: name must be a non-empty string.")
		# 	exit(1)
		# if not isinstance(cooking_lvl, int) or not (1 <= cooking_lvl <= 5):
		# 	print("Error: cooking_lvl must be an integer between 1 and 5.")
		# 	exit(1)
		# if not isinstance(cooking_time, int) or cooking_time < 0:
		# 	print("Error: cooking_time must be a non-negative integer.")
		# 	exit(1)
		# if not isinstance(ingredients, list) or not all(isinstance(i, str) and i for i in ingredients):
		# 	print("Error: ingredients must be a list of non-empty strings.")
		# 	exit(1)
		# if not isinstance(description, str):
		# 	print("Error: description must be a string.")
		# 	exit(1)
		# if recipe_type not in ["starter", "lunch", "dessert"]:
		# 	print("Error: recipe_type must be 'starter', 'lunch', or 'dessert'.")
		# 	exit(1)

		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self) -> str:
		"""Return the string to print with the recipe info"""
		txt = f"Recipe for {self.name}:\n"
		txt += f"Level: {self.cooking_lvl}\n"
		txt += f"Time: {self.cooking_time} min\n"
		txt += f"Ingredients: {', '.join(self.ingredients)}\n"
		txt += f"Description: {self.description}\n"
		txt += f"Recipe type: {self.recipe_type}\n"
		return txt


