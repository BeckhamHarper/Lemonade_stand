import Money_functions

# Function for changing the recipe
def recipe_changer(recipe, ingredients):
    if Money_functions.starting_question == "change the recipe":
        try:
            print("\nYou have,", ingredients["lemons"], "lemons")
            recipe_lemon = input("How many lemons do you want in your lemonade the minimum is 1 lemons max is 4,\n")
            if int(recipe_lemon) > 4 or int(recipe_lemon) < 1:
                print("Not a valid number of lemons")
                recipe["lemons for recipe"] = recipe_lemon
            else:    
                recipe["lemons for recipe"] = recipe_lemon
                print("You have",recipe['lemons for recipe'], "lemons in your recipe")
            
            print("\nYou have,", ingredients["sugar"], "tsps of sugar")
            recipe_sugar = input("How many tps of sugar do you want in your lemonade the minimum is 1 lemons max is 4,\n")
            if int(recipe_sugar) > 4 or int(recipe_sugar) < 1:
                print("Not a valid number of tps for sugar")
                recipe["sugar for recipe"] = recipe_sugar
            else:    
                recipe["sugar for recipe"] = recipe_sugar
                print("You have",recipe['sugar for recipe'], "tps of sugar in your recipe")

            print("\nYou have,", ingredients["ice_cups"], "ice cubes")
            recipe_ice_cups = input("How many ice cubes do you want in your lemonade the minimum is 1 lemons max is 4,\n")
            if int(recipe_ice_cups) > 4 or int(recipe_ice_cups) < 1:
                print("Not a valid number of ice cubes")
                recipe["ice_cups for recipe"] = recipe_ice_cups
            else:    
                recipe["ice_cups for recipe"] = recipe_ice_cups
                print("You have",recipe['ice_cups for recipe'], "ice cubes in your recipe\n")
        except ValueError:
            print("Not a valid amount")
# Function for setting the price of the cups!
def cup_price():
    try:
        price = float(input("What do you want the price for the lemonade to be?\n"))
        return price
    except ValueError:
        print("Please enter a valid price.")
        return -1