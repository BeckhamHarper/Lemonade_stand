money= 0
earnings = 0
purchases = 0
lemons = 0
sugar = 0
ice_cups = 0
priceForIce_cups = 2
difficulty = input("What difficulty would you like to do, Easy(1), Normal(2), Hard(3) or Alejandro(4? ")




def money_setter(difficulty):
    global money
    if difficulty == "Easy" or "1":
        money += 450
        print("You have "+ str(money) + " dollars")
    elif difficulty == "Normal" or "2":
        money += 300
        print("You have "+ str(money) + " dollars")
    elif difficulty == "Hard" or "3":
        money += 150
        print("You have "+ str(money) + " dollars")
    elif difficulty == "Alejandro"or "4":
        money += 1000
        print("You have "+ str(money) + " dollars")
    else:
        print("Ending game")
        exit()




money_setter(difficulty)




def mainQuestion():
    global starting_question
    starting_question = input("Would you like to start day(1), go to shop(2), set the price(3), change the recipe(4), or check ingredients(5)? ")




def shopQuestions(starting_question):
    global lemons, sugar, ice_cups, money
    if starting_question == "go to shop" or "2":
        items = input("Would you like to buy lemons(1), sugar(2), or ice_cups(3)? ")
   
        if items == "lemons" or "1":
            bought_lemons = input("1$ for 5 lemons, how many do you want to buy? ")
            priceForLemons = bought_lemons
            money -= int(bought_lemons)
            if money < 0:
                money += int(bought_lemons)
                print("Not enough money.")
            elif money > 0:
                lemons += int(bought_lemons)*5
                print("You now have", money, "dollars and ", lemons, " lemons? ")
   
        if items == "sugar" or "2":
            bought_sugar = input("1$ for 100 tsp of sugar, how many pounds do you want to buy")
            priceForSugar = bought_sugar
            money -= int(bought_sugar)
            if money < 0:
                money += int(bought_sugar)
                print("Not enough money.")
            elif money > 0:
                sugar += int(bought_sugar)*100
                print("You now have", money, "dollars and ", sugar, " sugar")
   
        if items == "ice_cups" or "3":
            bought_ice_cups = int(input("1$ for 100 ice cubes, how many bags do you want to buy"))
            priceForIce_cups = (bought_ice_cups)
            money -= int(priceForIce_cups)
            if money < 0:
                money += int(bought_ice_cups)
                print("Not enough money.")
            elif money > 0:
                ice_cups +=int(bought_ice_cups)*100
                print("You now have", money, "dollars and ", ice_cups, " ice cubes")




current_choice = mainQuestion()
shopQuestions(starting_question)



