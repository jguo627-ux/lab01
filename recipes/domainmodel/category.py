class Category:
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name
        self.__recipes = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name.strip()

    @property
    def recipes(self) -> list:
        return self.__recipes.copy()

    def add_recipe(self, recipe):
        if recipe not in self.__recipes:
            self.__recipes.append(recipe)

    def remove_recipe(self, recipe):
        if recipe in self.__recipes:
            self.__recipes.remove(recipe)

    def get_recipe_count(self) -> int:
        return len(self.__recipes)

    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)