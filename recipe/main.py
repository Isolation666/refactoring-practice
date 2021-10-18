from recipe import Recipe


def create_recipe(name, chocolate=0,
                  coffee=0, milk=0,
                  sugar=0, price=0.0):
    recipe = Recipe(name)
    recipe.chocolate = chocolate
    recipe.coffee = coffee
    recipe.milk = milk
    recipe.sugar = sugar
    recipe.price = price
    return recipe


if __name__ == '__main__':
    print(create_recipe("Coffee with sugar", 0, 4, 0, 2, 30.0))
    print(create_recipe("Latte", 0, 3, 1, 2, 40.0))
    print(create_recipe("Hot Chocolate", 3, 0, 4, 2, 30.0))
