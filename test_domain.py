from recipes.domainmodel.recipe import Recipe
from recipes.domainmodel.category import Category


def main():
    print("=== Testing Recipe Domain Model ===")

    dessert = Category(1, "Desserts")
    vegan = Category(2, "Vegan")
    print(f"Created: {dessert}")
    print(f"Created: {vegan}")

    cake = Recipe(101, "Chocolate Cake", "Chef John", "Delicious chocolate cake")
    salad = Recipe(102, "Vegan Salad", "Chef Jane", "Healthy vegan salad")
    print(f"Created: {cake}")
    print(f"Created: {salad}")

    cake.preparation_time = 20
    cake.cooking_time = 30
    cake.servings = 8

    salad.preparation_time = 10
    salad.cooking_time = 0
    salad.servings = 2

    print(f"Cake total time: {cake.total_time} minutes")
    print(f"Salad total time: {salad.total_time} minutes")

    cake.add_ingredient("2 cups flour")
    cake.add_ingredient("1 cup sugar")
    cake.add_ingredient("1/2 cup cocoa powder")

    salad.add_ingredient("Mixed greens")
    salad.add_ingredient("Cherry tomatoes")
    salad.add_ingredient("Cucumber")

    print(f"Cake ingredients: {cake.ingredients}")
    print(f"Salad ingredients: {salad.ingredients}")

    cake.add_instruction("Preheat oven to 350°F")
    cake.add_instruction("Mix dry ingredients")
    cake.add_instruction("Bake for 30 minutes")

    salad.add_instruction("Wash vegetables")
    salad.add_instruction("Chop and mix")

    print(f"Cake instructions: {len(cake.instructions)} steps")
    print(f"Salad instructions: {len(salad.instructions)} steps")

    cake.add_category(dessert)
    salad.add_category(vegan)

    print(f"Cake categories: {[c.name for c in cake.categories]}")
    print(f"Salad categories: {[c.name for c in salad.categories]}")
    print(f"Recipes in Desserts: {[r.name for r in dessert.recipes]}")
    print(f"Recipes in Vegan: {[r.name for r in vegan.recipes]}")

    print("=== Test Completed Successfully! ===")


if __name__ == "__main__":
    main()