import Money_functions as money
import recipe as recipe_functions
from customer_class import Customer
import day
from day import days

ingredients = {
    "lemons": 0,
    "sugar": 0,
    "ice_cups": 0
}
recipe_dict = {
    "lemons for recipe": 1,
    "sugar for recipe": 1,
    "ice_cups for recipe": 1
}
price_cup = 0

money.money = money.money_setter(input("What difficulty would you like to do, Easy, Normal, Hard or Alejandro? "))
print(f"You have {money.money} dollars")

if days < 8:
    running = 1
else:
    print("Game over! You completed 7 days of running your lemonade stand.")
    running = 0


while running == 1:
        q = (money.mainQuestion())
        if q == "go to shop":
            money.shopQuestions(q, money.money, ingredients)
        elif q == "set the price":
            recipe_functions.cup_price()
        elif q == "change the recipe":
            recipe_functions.recipe_changer(recipe_dict)
        elif q == "check ingredients":
            print("\nYou have", money.money, "dollars,", money.lemons,"lemons,", money.sugar, "tsps of sugar,", money.ice_cups, "ice cubes.\nYoure recipe consists of", recipe_dict["lemons for recipe"], "lemons", recipe_dict["sugar for recipe"], "tsps of sugar, and", recipe_dict["ice_cups for recipe"], "ice cubes.\nYoure price for cups is", recipe_functions.price_cup, "dollars.\n")
        elif q == "start day":
            recipe_functions.number_cups(ingredients, recipe_dict)
            day.startDay(q)
            user_input = input("Type 'stop' to end the game or press Enter to continue: ")
            if user_input.lower() == "stop":
                print("Game ended.")
                break
        else:
            print("Invalid option. Please try again.")