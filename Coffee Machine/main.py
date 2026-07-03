from art import logo

print(logo)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}





def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
    
    
    
def is_resources_sufficient(order_ingredients):
    
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is no enough {item}")
    return True
        

def process_coins():
    
    print("Please insert coins.")
    
    quarters = int(input("How many quarters?: ")) 
    dimes = int(input("How many dimes?: ")) 
    nickels = int(input("How many nickels?: ")) 
    pennies = int(input("How many pennies?: ")) 
    
    total = (
        quarters * 0.25,
        dimes * 0.10,
        nickels * 0.05,
        pennies * 0.01
    )
    
    return sum(total)


def is_transaction_susccessful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!😄.")


is_on = True

while is_on:
    print("Welcome to the Coffee Machine!🧋")
    print("Here are the available options:")
    for item in MENU:
        print(f"- {item.capitalize()}")
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        
        is_on = False
        
    elif choice == "report":
        
        print_report()
        
    elif choice not in MENU:
        
        print("Sorry, that item is not currently available . Please try again.")
        
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            
            payment = process_coins()
            
            if is_transaction_susccessful(payment, drink["cost"]):
                
                make_coffee(choice, drink["ingredients"])
                