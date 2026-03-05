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
    starting_question = input("Would you like to start day, go to shop, set the price, change the recipe, or check ingredients?\n")


def mainQuestion():
    global starting_question
    starting_question = input("Would you like to start day, go to shop, set the price, change the recipe, or check ingredients?\n ")
    return starting_question


def shopQuestions(starting_question, cash, ingredients):
    # add cash and the recipe as parameters
    # have it call cash where it calls money
    # Have it call the dictionary values instead of the hardcode values
    if starting_question == "go to shop":
        #Add it to where people can't buy negative number of items
        while True:
            try:
                items = input("Would you like to buy lemons, sugar, or ice_cups? ")
                if items == "lemons":
                    bought_lemons = int(input("1$ for 5 lemons, how many do you want to buy? "))
                    if bought_lemons > 0:
                        priceForLemons = bought_lemons
                        cash -= int(bought_lemons)
                        if cash < 0:
                            cash += int(bought_lemons)
                            print("Not enough money.")
                        elif cash >= 0:
                            ingredients["lemons"] += int(bought_lemons)*5
                            print(f"You now have {cash} dollars and {ingredients['lemons']} lemons.")
                    else:
                        print("Not a valid number to buy")
                        continue


                if items == "sugar":
                    bought_sugar = int(input("1$ for 100 tsp of sugar, how many pounds do you want to buy"))
                    if bought_sugar > 0:
                        priceForSugar = bought_sugar
                        cash -= int(bought_sugar)
                        if cash < 0:
                            cash += int(bought_sugar)
                            print("Not enough money.")
                        elif cash >= 0:
                            ingredients["sugar"] += int(bought_sugar)*100
                            print("You now have", cash, "dollars and ", ingredients["sugar"], " sugar")
                    else:
                        print("Not a valid number to buy")
                        continue


                if items == "ice_cups":
                    bought_ice_cups = int(input("1$ for 100 ice cubes, how many bags do you want to buy"))
                    if bought_ice_cups > 0:
                        priceForIce_cups = (bought_ice_cups)
                        cash -= int(priceForIce_cups)
                        if cash < 0:
                            cash += int(bought_ice_cups)
                            print("Not enough money.")
                        elif cash >= 0:
                            ingredients["ice_cups"] +=int(bought_ice_cups)*100
                            print("You now have", cash, "dollars and ", ingredients["ice_cups"], " ice cubes")
                    else:
                        print("Not a valid number to buy")
                        continue

            except ValueError:
                print("Not a valid amount")
                continue
            if items != "lemons" and items != "sugar" and items != "ice_cups":
                print("Not a valid option try again.")
                continue
            continue_shopping = input("Type 'stop' to stop shopping or press Enter to continue shopping: ")
            if continue_shopping.lower() == "stop":
                return cash
