from money_function import money_setter, mainQuestion, shopQuestions
import recipe
from customer_class import Customer
import day
def func_ingredients():
    global ingredients
    ingredients = {
        "lemons": 0,
        "sugar": 0,
        "ice_cups": 0
    }

recipe1 = {
    "lemons for recipe": 1,
    "sugar for recipe": 1,
    "ice_cups for recipe": 1
}
price_cup = 0

cash = money_setter(input("What difficulty would you like to do, Easy, Normal, Hard or Alejandro? "))
print(f"You have {cash} dollars")

cash = money_function.money_setter(input("What difficulty would you like to do, Easy, Normal, Hard or Alejandro? "))
print(f"You have {cash} dollars")

while True:
    q = (money_function.mainQuestion())

    if q == "go to shop":
        money_function.shopQuestions(q, cash, ingredients)

    elif q == "set the price":
        recipe.cup_price()

    elif q == "change the recipe":
        recipe.recipe_changer(recipe1)

    elif q == "check ingredients":
        print("You have", cash, "dollars,", ingredients["lemons"],"lemons,", ingredients["sugar"], "tsps of sugar,", ingredients['ice_cups'], "ice cubes.\nYoure recipe consists of", recipe1["lemons for recipe"], "lemons", recipe1["sugar for recipe"], "tsps of sugar, and", recipe1["ice_cups for recipe"], "ice cubes.\nYoure price for cups is", price_cup, "dollars.\n")

    elif q == "start day":
        day.startDay(q)
        user_input = input("Type 'stop' to end the game or press Enter to continue: ")
        if user_input.lower() == "stop":
            print("Game ended.")
            break
        
    else:
        print("Invalid option. Please try again.")
    # recipe.number_cups()