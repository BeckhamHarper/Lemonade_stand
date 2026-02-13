import money
import recipe
from customer_class import Customer
import day


while True:

    money.mainQuestion()
    if money.starting_question == "go to shop":
        money.shopQuestions(money.starting_question)
    elif money.starting_question == "set the price":
        recipe.cup_price()
    elif money.starting_question == "change the recipe":
        recipe.recipe_changer()
    elif money.starting_question == "check ingredients":
        print("You have", money.money, "dollars,", money.lemons,"lemons,", money.sugar, "tsps of sugar,", money.ice_cups, "ice cubes.\nYoure recipe consists of", recipe["lemons for recipe"], "lemons", recipe["sugar for recipe"], "tsps of sugar, and", recipe["ice_cups for recipe"], "ice cubes.\nYoure price for cups is", price_cup, "dollars.\n")
    elif money.starting_question == "start day":
        day.startDay
        user_input = input("Type 'stop' to end the game or press Enter to continue: ")
        if user_input.lower() == "stop":
            print("Game ended.")
            break
    else:
        print("Invalid option. Please try again.")
    recipe.number_cups()
