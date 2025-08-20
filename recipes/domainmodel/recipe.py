class Recipe:
    def __init__(self, recipe_id, name, author, description=""):
        self._id = recipe_id
        self._name = name
        self._author = author
        self._description = description
        self._ingredients = []
        self._instructions = []
        self._cook_time = 0
        self._prep_time = 0
        self._servings = 0
        self._categories = []
        self._reviews = []

    def add_ingredient(self, ingredient):
        if ingredient and ingredient not in self._ingredients:
            self._ingredients.append(ingredient)

    def add_instruction(self, instruction):
        if instruction:
            self._instructions.append(instruction)

    def add_category(self, category):
        if category not in self._categories:
            self._categories.append(category)
            category.add_recipe(self)

    def __str__(self):
        return f"Recipe {self._id}: {self._name}"