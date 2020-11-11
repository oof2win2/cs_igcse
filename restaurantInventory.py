def printMenu(menu):
    for key in menu:
        print(f"Option number {key}: {menu[key]}")

def placeOrder(menu):
    order = {}
    for key in menu:
        num = input(f"How much of option number {key}: ")
        order[key] = int(num)
    return order

def printOrder(order):
    for key in order:
        if (order[key] != 0):
            print(f"Order of item number {key}: {order[key]} times")

def calcProfits(order, menuPrices, profitMargin):
    # profit margin is a percentage (whole number), such as 50% = 0.50
    profit = 0.00
    totalCost = 0
    for item in order:
        if (order[item] != 0):
            for i in range(order[item]):
                profit += (menuPrices[item])*profitMargin
                totalCost += menuPrices[item]
    return profit

def run():
    menu = {
        70: "French fries",
        71: "1/4 pound burger",
        72: "1/4 pound cheeseburger",
        73: "1/2 pound burger",
        74: "1/2 pound cheeseburger",
        75: "medium pizza",
        76: "medium pizza with extra toppings",
        77: "large pizza",
        78: "large pizza with extra toppings",
        79: "garlic bread"
    }
    menuPrices = {
        70:  2.00,
        71:  5.00,
        72:  5.55,
        73:  7.00,
        74:  7.50,
        75:  9.00,
        76: 11.00,
        77: 12.00,
        78: 14.50,
        79:  4.50,
    }
    printMenu(menu)
    order = placeOrder(menu)
    printOrder(order)
    profit = calcProfits(order, menuPrices, 0.10)
    print(profit)

if __name__ == "__main__":
    run()