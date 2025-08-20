class Category:
    def __init__(self, cid, name):
        self.id = cid
        self.name = name
        self.recipes = []

    def add_recipe(self, recipe):
        if recipe not in self.recipes:
            self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)

    def __str__(self):
        return f"Category {self.id}: {self.name}"