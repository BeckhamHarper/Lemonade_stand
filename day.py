import money_function as money
from customer_class import Customer
import recipe

days = 0

def startDay(starting_question, ingredients, recipe, cash, price_cup):
    global days
    if starting_question == "start day":
        days += 1
        earnings = 0
        cups_sold = 0
        num_customers = 10
        customers = []
            
        # At start of the day, calculate how many cups can be made with current ingredients
        cups_for_lemons = ingredients["lemons"] / int(recipe["lemons for recipe"])
        cups_for_sugar = ingredients["sugar"] / int(recipe["sugar for recipe"])
        cups_for_ice_cups = ingredients["ice_cups"] / int(recipe["ice_cups for recipe"])
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
            if (sweetness >= int(recipe["lemons for recipe"]) and
                ice >= int(recipe["ice_cups for recipe"]) and
                price >= price_cup):
                # Deduct ingredients used for one cup
                ingredients["lemons"] -= int(recipe["lemons for recipe"])
                ingredients["sugar"] -= int(recipe["sugar for recipe"])
                ingredients["ice_cups"] -= int(recipe["ice_cups for recipe"])
                available_cups -= 1
                cups_sold += 1
                earnings += price_cup
                print(f"Customer bought lemonade for ${price_cup}")
            else:
                print("Customer did not buy lemonade.")
        
        # Add earnings to money and display summary of the day
        cash += earnings
        print(f"Day {days} Summary:")
        print(f"Cups sold: {cups_sold}")
        print(f"Day earnings: ${earnings}")
        print(f"Total money: ${cash}")
        print(f"Remaining ingredients: {ingredients['lemons']} lemons, {ingredients['sugar']} tsps of sugar, {ingredients['ice_cups']} ice cubes\n")
        print(f"End of day, {days}.\n")
    return cash