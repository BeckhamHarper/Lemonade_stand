import Money_functions

# Function for changing the recipe
def recipe_changer(recipe, ingredients):
    if Money_functions.starting_question == "change the recipe":
        print("\nYou have,", ingredients["lemons"], "lemons")
        while True:
            try:
                recipe_lemon = int(input("How many lemons do you want in your lemonade? Minimum is 1, max is 4.\n"))
                if 1 <= recipe_lemon <= 4:
                    recipe["lemons for recipe"] = recipe_lemon
                    print("You have", recipe['lemons for recipe'], "lemons in your recipe")
                    break
                else:
                    print("Not a valid number of lemons")
            except ValueError:
                print("Not a valid amount")
        
        print("\nYou have,", ingredients["sugar"], "tsps of sugar")
        while True:
            try:
                recipe_sugar = int(input("How many tsps of sugar do you want in your lemonade? Minimum is 1, max is 4.\n"))
                if 1 <= recipe_sugar <= 4:
                    recipe["sugar for recipe"] = recipe_sugar
                    print("You have", recipe['sugar for recipe'], "tsps of sugar in your recipe")
                    break
                else:
                    print("Not a valid number of tsps for sugar")
            except ValueError:
                print("Not a valid amount")
        
        print("\nYou have,", ingredients["ice_cups"], "ice cubes")
        while True:
            try:
                recipe_ice_cups = int(input("How many ice cubes do you want in your lemonade? Minimum is 1, max is 4.\n"))
                if 1 <= recipe_ice_cups <= 4:
                    recipe["ice_cups for recipe"] = recipe_ice_cups
                    print("You have", recipe['ice_cups for recipe'], "ice cubes in your recipe\n")
                    break
                else:
                    print("Not a valid number of ice cubes")
            except ValueError:
                print("Not a valid amount")
# Function for setting the price of the cups!
def cup_price():
    price_input = input("What do you want the price for the lemonade to be?\n")
    if price_input.lower() == "stop":
        print("Price setting cancelled.")
        return -1
    try:
        price = float(price_input)
        if price <= 0:
            print("Price must be greater than 0.")
            return -1
        return price
    except ValueError:
        print("Please enter a valid price.")
        return -1