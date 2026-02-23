# money= 0
# earnings = 0
# purchases = 0
# lemons = 0
# sugar = 0
# ice_cups = 0
# priceForIce_cups = 2

# difficulty = input("What difficulty would you like to do, Easy, Normal, Hard or Alejandro? ")


def money_setter(difficulty):
    if difficulty.lower() == "easy":
        return 450

    elif difficulty.lower() == "normal":
        return 300

    elif difficulty.lower() == "hard":
        return 150

    elif difficulty.lower() == "alejandro":
        return 1000

    else:
        print("Ending game")
        exit()





def mainQuestion():
    starting_question = input("Would you like to start day, go to shop, set the price, change the recipe, or check ingredients? ")
    return starting_question



def shopQuestions(starting_question, cash):
    # add cash and the recipe as parameters
    # have it call cash where it calls money
    # Have it call the dicitonary values instead of the hardcode values
    if starting_question == "go to shop":

        while True:
            items = input("Would you like to buy lemons, sugar, or ice_cups? ")

            if items == "lemons":
                bought_lemons = input("1$ for 5 lemons, how many do you want to buy? ")
                priceForLemons = bought_lemons
                money -= int(bought_lemons)
                if money < 0:
                    money += int(bought_lemons)
                    print("Not enough money.")
                elif money > 0:
                    lemons += int(bought_lemons)*5
                    print("You now have", money, "dollars and ", lemons, " lemons? ")

            if items == "sugar":
                bought_sugar = input("1$ for 100 tsp of sugar, how many pounds do you want to buy")
                priceForSugar = bought_sugar
                money -= int(bought_sugar)
                if money < 0:
                    money += int(bought_sugar)
                    print("Not enough money.")
                elif money > 0:
                    sugar += int(bought_sugar)*100
                    print("You now have", money, "dollars and ", sugar, " sugar")

            if items == "ice_cups":
                bought_ice_cups = int(input("1$ for 100 ice cubes, how many bags do you want to buy"))
                priceForIce_cups = (bought_ice_cups)
                money -= int(priceForIce_cups)
                if money < 0:
                    money += int(bought_ice_cups)
                    print("Not enough money.")
                elif money > 0:
                    ice_cups +=int(bought_ice_cups)*100
                    print("You now have", money, "dollars and ", ice_cups, " ice cubes")
            continue_shopping = input("Type 'stop' to stop shopping or press Enter to continue shopping: ")
            if continue_shopping.lower() == "stop":
                break






# current_choice = mainQuestion()
# shopQuestions(starting_question)



