import money
import recipe
from customer_class import Customer
import day


cash = money.money_setter(input("What difficulty would you like to do, Easy, Normal, Hard or Alejandro? "))
print(f"You have {cash} dollars")

while True:
    q = (money.mainQuestion())
    if q == "go to shop":
        money.shopQuestions(q)
    elif q == "set the price":
        recipe.cup_price()
    elif q == "change the recipe":
        recipe.recipe_changer()
    elif q == "check ingredients":
        print("You have", cash, "dollars,", money.lemons,"lemons,", money.sugar, "tsps of sugar,", money.ice_cups, "ice cubes.\nYoure recipe consists of", recipe.recipe["lemons for recipe"], "lemons", recipe.recipe["sugar for recipe"], "tsps of sugar, and", recipe.recipe["ice_cups for recipe"], "ice cubes.\nYoure price for cups is", recipe.price_cup, "dollars.\n")
    elif q == "start day":
        day.startDay
        user_input = input("Type 'stop' to end the game or press Enter to continue: ")
        if user_input.lower() == "stop":
            print("Game ended.")
            break
    else:
        print("Invalid option. Please try again.")
    recipe.number_cups()