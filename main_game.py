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
        print(f"You have {money.money} dollars, {money.lemons} lemons, {money.sugar} tsps of sugar, {money.ice_cups} ice cubes.")
        print(f"Your recipe: {recipe.recipe['lemons for recipe']} lemons, {recipe.recipe['sugar for recipe']} tsps sugar, {recipe.recipe['ice_cups for recipe']} ice cubes.")
        print(f"Price per cup: {recipe.price_cup}")
    elif money.starting_question == "start day":
        day.startDay
        user_input = input("Type 'stop' to end the game or press Enter to continue: ")
        if user_input.lower() == "stop":
            print("Game ended.")
            break
    else:
        print("Invalid option. Please try again.")
    recipe.number_cups()
