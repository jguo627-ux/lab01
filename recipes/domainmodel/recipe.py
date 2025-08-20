from datetime import datetime

class Recipe:
    def __init__(self, id: int, name: str, author: str, description: str = ""):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__description = description
        self.__ingredients = []
        self.__instructions = []
        self.__categories = []
        self.__cooking_time = 0
        self.__preparation_time = 0
        self.__servings = 0
        self.__rating = 0.0
        self.__reviews = []
        self.__date_added = datetime.now()
        self.__images = []

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
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, new_author: str):
        if isinstance(new_author, str) and new_author.strip():
            self.__author = new_author.strip()

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description: str):
        if isinstance(new_description, str):
            self.__description = new_description

    @property
    def ingredients(self) -> list:
        return self.__ingredients.copy()

    @property
    def instructions(self) -> list:
        return self.__instructions.copy()

    @property
    def categories(self) -> list:
        return self.__categories.copy()

    @property
    def cooking_time(self) -> int:
        return self.__cooking_time

    @cooking_time.setter
    def cooking_time(self, minutes: int):
        if isinstance(minutes, int) and minutes >= 0:
            self.__cooking_time = minutes

    @property
    def preparation_time(self) -> int:
        return self.__preparation_time

    @preparation_time.setter
    def preparation_time(self, minutes: int):
        if isinstance(minutes, int) and minutes >= 0:
            self.__preparation_time = minutes

    @property
    def total_time(self) -> int:
        return self.preparation_time + self.cooking_time

    @property
    def servings(self) -> int:
        return self.__servings

    @servings.setter
    def servings(self, count: int):
        if isinstance(count, int) and count > 0:
            self.__servings = count

    def add_ingredient(self, ingredient: str):
        if isinstance(ingredient, str) and ingredient.strip() and ingredient not in self.__ingredients:
            self.__ingredients.append(ingredient.strip())

    def add_instruction(self, instruction: str):
        if isinstance(instruction, str) and instruction.strip():
            self.__instructions.append(instruction.strip())

    def add_category(self, category):
        if category not in self.__categories:
            self.__categories.append(category)
            category.add_recipe(self)

    def __repr__(self):
        return f"<Recipe {self.id}: {self.name} by {self.author}>"

    def __eq__(self, other):
        if not isinstance(other, Recipe):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)