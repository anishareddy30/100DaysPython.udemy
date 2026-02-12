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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def if_resources_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            return False
        return True
    
def process_coins():
    total = int(input("how many quarters : ")) * 0.25
    total += int(input ("how many dimes :")) * 0.10
    total += int(input("how many nickles :")) * 0.05
    total += int(input ("how many pennies :")) *0.01
    return total

def check_transaction_successfull (money_received ,drink_cost ) :
    change  = round(money_received - drink_cost)
    if money_received > drink_cost:
        print(f"here is your{change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("money is not sufficient")
        return False

def make_coffee():
    resources - 



    
