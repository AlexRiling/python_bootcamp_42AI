import datetime

class Book:
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.datetime.now
		self.creation_date = datetime.datetime.now
		self.recipes_list = {"starter": [], "lunch": [], "dessert": []}


	def get_recipe_by_name(self, name):
	# "Prints a recipe with the name \texttt{name} and returns the instance"
		for recipes in self.recipes_list.values():
			for recipe in recipes:
				if recipe.name == name:
					print(recipe)
					return recipe
		print(f"Recipe '{name}' not found.")
		return None


	def get_recipes_by_types(self, recipe_type):
	# "Get all recipe names for a given recipe_type"
		if recipe_type in self.recipes_list:
			return [recipe.name for recipe in self.recipes_list[recipe_type]]
		else:
			print("Error: Invalid recipe type.")
			return []


	def add_recipe(self, recipe):
		# "Add a recipe to the book and update last_update"
		# if not isinstance(recipe, Recipe):
		# 	print("Error: The argument must be an instance of Recipe.")
		# 	return
		if recipe.recipe_type in self.recipes_list:
			self.recipes_list[recipe.recipe_type].append(recipe)
			self.last_update = datetime.datetime.now()
		else:
			print("Error: Invalid recipe type.")

