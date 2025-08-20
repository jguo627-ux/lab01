from recipes.domainmodel.recipe import Recipe
from recipes.domainmodel.category import Category


def test_recipes():
    print("Testing Recipe System")
    print("-" * 30)

    cake = Recipe(101, "Chocolate Cake", "Chef John")
    cake.add_ingredient("Flour")
    cake.add_ingredient("Sugar")
    cake.cook_time = 45

    salad = Recipe(102, "Vegan Salad", "Chef Jane")
    salad.add_ingredient("Lettuce")
    salad.add_ingredient("Tomato")
    salad.cook_time = 10

    dessert_cat = Category(1, "Desserts")
    healthy_cat = Category(2, "Healthy")

    dessert_cat.add_recipe(cake)
    healthy_cat.add_recipe(salad)

    print("Recipes:")
    print(cake)
    print(salad)

    print("\nCategories:")
    print(dessert_cat)
    print(healthy_cat)

    print(f"\nDesserts: {len(dessert_cat.recipes)} recipe")
    print(f"Healthy: {len(healthy_cat.recipes)} recipe")


if __name__ == "__main__":
    test_recipes()