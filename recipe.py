import money
ingredients = {
    "lemons": money.lemons,
    "sugar": money.sugar,
    "ice_cups": money.ice_cups
}
recipe = {
    "lemons for recipe": 1,
    "sugar for recipe": 1,
    "ice_cups for recipe": 1
}
price_cup = 0
money.money_setter

def recipe_changer():
    if money.starting_question == "change the recipe":
        print("You have,", money.lemons, "lemons")
        
        recipe_lemon = input("How many lemons do you want in your lemonade the minimum is 1 lemons max is 4,\n")
        if int(recipe_lemon) > 4 or int(recipe_lemon) < 1:
            print("Not a valid number of lemons")
            recipe["lemons for recipe"] = recipe_lemon
        else:    
            recipe["lemons for recipe"] = recipe_lemon
            print("You have",recipe['lemons for recipe'], "lemons in your recipe")
        
        print("You have,", money.sugar, "tsps of sugar")
        recipe_sugar = input("How many tps of sugar do you want in your lemonade the minimum is 1 lemons max is 4,\n")
        if int(recipe_sugar) > 4 or int(recipe_sugar) < 1:
            print("Not a valid number of tps for sugar")
            recipe["sugar for recipe"] = recipe_sugar
        else:    
            recipe["sugar for recipe"] = recipe_sugar
            print("You have",recipe['sugar for recipe'], "tps of sugar in your recipe")

        print("You have,", money.ice_cups, "ice cubes")
        recipe_ice_cups = input("How many ice cubes do you want in your lemonade the minimum is 1 lemons max is 4,\n")
        if int(recipe_ice_cups) > 4 or int(recipe_ice_cups) < 1:
            print("Not a valid number of ice cubes")
            recipe["ice_cups for recipe"] = recipe_ice_cups
        else:    
            recipe["ice_cups for recipe"] = recipe_ice_cups
            print("You have",recipe['ice_cups for recipe'], "ice cubes in your recipe")

def cup_price():
    global price_cup
    if money.starting_question == "set the price":
        price_cup = float(input("What do you want the price for the lemonade to be?\n"))
recipe_changer()
cup_price()

print("You have", money.money, "dollars,", money.lemons,"lemons,", money.sugar, "tsps of sugar,", money.ice_cups, "ice cubes.\nYoure recipe consists of", recipe["lemons for recipe"], "lemons", recipe["sugar for recipe"], "tsps of sugar, and", recipe["ice_cups for recipe"], "ice cubes.\nYoure price for cups is", price_cup, "dollars.\n")

def number_cups():
    cups_for_lemons = ingredients["lemons"]/recipe["lemons for recipe"]
    cups_for_sugar = ingredients["sugar"]/recipe["sugar for recipe"]
    cups_for_ice_cups = ingredients["ice_cups"]/recipe["ice_cups for recipe"]
    print(cups_for_lemons, cups_for_sugar,cups_for_ice_cups)
    return min(cups_for_lemons,cups_for_ice_cups,cups_for_sugar)
number_cups()