def shopping_cart(*args):
    meals = {"Soup": [], "Pizza": [], "Dessert": []}
    result_ = ""
    for el in args:
        meals_values = (meals["Soup"], meals["Pizza"], meals["Dessert"])
        if el == "Stop":
            if not any(meals_values):
                return "No products in the cart!"
            else:
                break

        else:
            if el[0] not in meals:
                meals[el[0]] = meals.get(el[0], []) + [el[1]]

            elif el[0] == "Soup" and len(meals["Soup"]) < 3 and el[1] not in meals[el[0]]:
                meals[el[0]] = meals.get(el[0], []) + [el[1]]

            elif el[0] == "Pizza" and len(meals["Pizza"]) < 4 and el[1] not in meals[el[0]]:
                meals[el[0]] = meals.get(el[0], []) + [el[1]]

            elif el[0] == "Dessert" and len(meals["Dessert"]) < 2 and el[1] not in meals[el[0]]:
                meals[el[0]] = meals.get(el[0], []) + [el[1]]
            
    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    for m, p in sorted_meals:
        result_ += m + ":" + "\n"
        for elem in sorted(p):
            result_ += " - " + elem + "\n"
    return result_


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
