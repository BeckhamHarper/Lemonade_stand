import money_function
from customer_class import Customer
import recipe
days = 1

def startDay(starting_question):
    if starting_question == "start day":
        earnings = 0
        cups_sold = 0
        num_customers = 10
        customers = []
        
        # At start of the day, calculate how many cups can be made with current ingredients
        cups_for_lemons = money_function.lemons / int(recipe.recipe["lemons for recipe"])
        cups_for_sugar = money_function.sugar / int(recipe.recipe["sugar for recipe"])
        cups_for_ice_cups = money_function.ice_cups / int(recipe.recipe["ice_cups for recipe"])
        available_cups = int(min(cups_for_lemons, cups_for_sugar, cups_for_ice_cups))
        
        print(f"You can make {available_cups} cups of lemonade today!\n")
        
        # Creats the customers
        for i in range(num_customers):
            customers.append(Customer())
        
        for customer in customers:
            if available_cups <= 0:
                print("Out of cups! No more sales today.")
                break
            
            attributes = customer.get_customer_attributes()
            sweetness = attributes["sweetness"]
            ice = attributes["ice"]
            price = attributes["price"]
            
            # Checks if customers buys the lemonade
            if (sweetness >= int(recipe.recipe["lemons for recipe"]) and
                ice >= int(recipe.recipe["ice_cups for recipe"]) and
                price >= recipe.price_cup):
                # Deduct ingredients used for one cup
                money_function.lemons -= int(recipe.recipe["lemons for recipe"])
                money_function.sugar -= int(recipe.recipe["sugar for recipe"])
                money_function.ice_cups -= int(recipe.recipe["ice_cups for recipe"])
                available_cups -= 1
                cups_sold += 1
                earnings += recipe.price_cup
                print(f"Customer bought lemonade for ${recipe.price_cup}")
            else:
                print("Customer did not buy lemonade.")
        
        # Add earnings to money and display summary of the day
        money_function.money += earnings
        print("Day Summary:")
        print(f"Cups sold: {cups_sold}")
        print(f"Day earnings: ${earnings}")
        print(f"Total money: ${money_function.money}")