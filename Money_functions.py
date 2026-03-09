# Function for setting the starting money
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
        print("Not a valid difficulty. Ending game.")
        exit()

def mainQuestion():
    global starting_question
    starting_question = input("Would you like to start day, go to shop, set the price, change the recipe, or check ingredients?\n ")
    return starting_question

def bankruptcy_check():
    print("You have lost all your money! Game over.")
    exit()

def shopQuestions(starting_question, cash, ingredients):
    valid_responses = ["lemons","ice_cups","sugar"]
    if starting_question == "go to shop":
        while True:
            try:
                items = input("Would you like to buy lemons, sugar, or ice_cups? If you want to leave then type 'stop'\n")
                if items == "stop":
                    return cash
                if items == "lemons":
                    while items in valid_responses:
                        try:
                            bought_lemons = input("1$ for 5 lemons, how many do you want to buy? If you want to leave then type 'stop'\n")
                            if bought_lemons.lower() == "stop":
                                break
                            bought_lemons = int(bought_lemons)
                        except ValueError:
                            print("Not a valid amount")
                            continue
                        if bought_lemons > 0:
                            cash -= int(bought_lemons)
                            if cash <= 0:
                                bankruptcy_check()
                            elif cash > 0:
                                ingredients["lemons"] += int(bought_lemons)*5
                                print(f"You now have {cash} dollars and {ingredients['lemons']} lemons.")
                                break
                        elif bought_lemons == "stop":
                            break
                        else:
                            print("Not a valid number to buy")
                            continue


                if items == "sugar":
                    while items in valid_responses:
                        try:
                            bought_sugar = input("1$ for 100 tsp of sugar, how many pounds do you want to buy? If you want to leave then type 'stop'\n")
                            if bought_sugar.lower() == "stop":
                                break
                            bought_sugar = int(bought_sugar)
                        except ValueError:
                            print("Not a valid amount")
                            continue
                        if bought_sugar > 0:
                            cash -= int(bought_sugar)
                            if cash <= 0:
                                bankruptcy_check()
                            elif cash > 0:
                                ingredients["sugar"] += int(bought_sugar)*100
                                print("You now have", cash, "dollars and", ingredients["sugar"], "sugar")
                                break
                        else:
                            print("Not a valid number to buy")
                            continue


                if items == "ice_cups":
                    while items in valid_responses:
                        try:
                            bought_ice_cups = input("1$ for 100 ice cubes, how many bags do you want to buy? If you want to leave then type 'stop'\n")
                            if bought_ice_cups.lower() == "stop":
                                break
                            bought_ice_cups = int(bought_ice_cups)
                        except ValueError:
                            print("Not a valid amount")
                            continue
                        if bought_ice_cups > 0:
                            cash -= int(bought_ice_cups)
                            if cash <= 0:
                                bankruptcy_check()
                            elif cash > 0:
                                ingredients["ice_cups"] += int(bought_ice_cups)*100
                                print("You now have", cash, "dollars and", ingredients["ice_cups"], "ice cubes")
                                break
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
    return cash