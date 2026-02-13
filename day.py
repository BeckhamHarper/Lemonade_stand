import money
from customer_class import Customer
import recipe
days = 1
customers = []

for i in range(10):
    customers.append(Customer())

for each in customers:
    attributes = each.get_customer_attributes()
    print(attributes)


def startDay(starting_question):
    if money.starting_question() == "start day":

        while days < 8:

            if customers.get_customer_attributes()["sweetness"] >= recipe()["lemons for recipe"]:
                print("W")

            if customers.get_customer_attributes()["ice"] >= recipe()["ice_cups for recipe"]:
                print("W")
            
            if customers.get_customer_attributes()["price"] >= recipe.price_cup:
                print("Ok")
