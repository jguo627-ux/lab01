from recipes.domainmodel.recipe import Recipe
from recipes.domainmodel.category import Category
from datetime import datetime


def run_demo():
    print("Task 2 Demo - Recipe Categories")
    print("=" * 30)

    r1 = Recipe(7709, "Put Put Pie", "Rory Butterfield", "Sweet dessert")
    r1._Recipe__date_added = datetime(2024, 6, 29)

    r2 = Recipe(10643, "Pineapple Salas", "Diana Adams", "Fresh salad")
    r2._Recipe__date_added = datetime(2014, 8, 4)

    r3 = Recipe(12503, "Peas and Chicken", "Derrek", "Main course")
    r3._Recipe__date_added = datetime(2015, 10, 5)

    print("\nRecipes made:")
    print(f"- {r1}")
    print(f"- {r2}")
    print(f"- {r3}")

    cat1 = Category(101, "Asian")
    cat2 = Category(102, "Beth/Bury")
    cat3 = Category(87, "Thai")

    print(f"\nCategories: {cat1}, {cat2}, {cat3}")

    cat1.add_recipe(r1)
    cat1.add_recipe(r2)
    cat2.add_recipe(r3)

    tr1 = Recipe(3401, "Thai Sirtuin", "Dancer", "Spicy Thai")
    tr1._Recipe__date_added = datetime(2019, 10, 16)
    tr2 = Recipe(3402, "Thai Sweet", "Thai Chef", "Sweet Thai")
    tr2._Recipe__date_added = datetime(2020, 3, 15)

    cat3.add_recipe(tr1)
    cat3.add_recipe(tr2)

    print(f"\n{cat3.name} recipes:")
    for rec in cat3.recipes:
        print(f"  {rec}")


if __name__ == "__main__":
    run_demo()