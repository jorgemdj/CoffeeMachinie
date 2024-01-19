from coffemenu import MENU, resources

MENU["espresso"]["ingredients"]["milk"] = 0

# initial resources
resource = [["water", resources["water"]], ["milk", resources["milk"]], ["coffee", resources["coffee"]], 0]


def resource_get(recipe):
    recipe_water = MENU[recipe]["ingredients"]["water"]
    recipe_milk = MENU[recipe]["ingredients"]["milk"]
    recipe_coffee = MENU[recipe]["ingredients"]["coffee"]
    return [recipe_water, recipe_milk, recipe_coffee]


def report(item):
    print(f"Water: {item[0][1]}ml\nMilk: {item[1][1]}ml\nCoffee: {item[2][1]}g\nMoney: ${item[3]}")


def payment(order):
    order_cost = MENU[order]["cost"]
    return order_cost


def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))*0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickles = int(input("How many nickles?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01
    return pennies+nickles+dimes+quarters


def resource_enough(ingredients, order):
    enough = True
    missing = []
    for i in range(0, 3):
        if ingredients[i][1] < order[i]:
            enough = False
            missing.append(ingredients[i][0])
    return enough, missing


def drink_request():
    drink_unknown = True
    found = False
    request = ""
    while drink_unknown:
        request = str(input("What would you like? (espresso/latte/cappuccino): "))
        for key in MENU:
            if request == key or request == "report" or request == "off":
                found = True
        if not found:
            print("It wasn't found this drink in the data base. Choose a drink in the options above.")
        else:
            drink_unknown = False
    return request


def coffee_machine():

    machine_on = True

    while machine_on:

        request = drink_request()

        if request == "report":
            report(resource)
        elif request == "off":
            machine_on = False
        else:
            order = resource_get(request)
            profit = payment(request)
            missing = resource_enough(resource, order)[1]

            if resource_enough(resource, order)[0]:

                change = coins() - profit
                if change < 0:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    print(f"Here is ${change:.2f} in change.")
                    print(f"Here is your {request} ☕. Enjoy!")

                    for i in range(0, 3):
                        resource[i][1] -= resource_get(request)[i]

                    resource[3] += profit

            else:
                report_missing = ", ".join(missing)
                print(f"Sorry, there is not enough {report_missing}.")


coffee_machine()
