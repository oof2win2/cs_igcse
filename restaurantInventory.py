import random

def printMenu(menu):
    for key in menu:
        print(f"Option number {key}: {menu[key]}")

def placeOrder(menu):
    order = {}
    orderCode = random.randint(70, 91)
    for key in menu:
        try:
            num = input(f"How much of option number {key}: ")
            order[key] = int(num)
        except:
            print('error with order input. order cancelled')
            return {}, orderCode
    return order, orderCode

def printOrder(order, orderCode):
    for key in order:
        if (order[key] != 0):
            print(f"Order of item number {key}: {order[key]} times")
    print(f"order code: {orderCode}")

def calcProfits(order, menuPrices, profitMargin):
    # profit margin is a percentage (whole number), such as 50% = 0.50
    profit = 0.00
    totalCost = 0
    for item in order:
        if (order[item] != 0):
            for i in range(order[item]):
                profit += (menuPrices[item])*profitMargin
                totalCost += menuPrices[item]
    return profit, totalCost

def managerPrint(totalOrders):
    #init values
    totalIncome = 0.00
    totalProfit = 0.00
    numOrders = 0
    for i in range(len(totalOrders)): #do following for every order
        totalProfit += totalOrders[i][0] #add the profit
        totalIncome += totalOrders[i][1] #add the income
        numOrders += 1  #add 1 to the number of total orders
    #print the number of orders, total income and total profit
    print(f"total profit: {round(totalProfit, 2)}, total income: {round(totalIncome, 2)}, total orders: {numOrders}")

def run():
    menu = { # the menu itself
        1: "French fries",
        11: "1/4 pound burger",
        22: "1/4 pound cheeseburger",
        33: "1/2 pound burger",
        44: "1/2 pound cheeseburger",
        55: "medium pizza",
        66: "medium pizza with extra toppings",
        77: "large pizza",
        88: "large pizza with extra toppings",
        99: "garlic bread"
    }
    menuPrices = { #the prices of the menu
        1:   2.00,
        11:  5.00,
        22:  5.55,
        33:  7.00,
        44:  7.50,
        55:  9.00,
        66: 11.00,
        77: 12.00,
        88: 14.50,
        99:  4.50,
    }
    totalOrders = []
    while True:
        printMenu(menu) #print the menu first
        order = placeOrder(menu) #place the order
        printOrder(order[0], order[1]) #print the order and price
        profit = calcProfits(order[0], menuPrices, 0.10) #third parameter is profit margin in decimal
        totalOrders.append([profit[0], profit[1], order[1]]) #add the order to the total orders
        print(f"profit: ${round(profit[0], 3)}, total cost: ${round(profit[1])}") #print the profits
        choice = input("For new order enter 'n', for end of the day input 'e' ") #input for new order/manager
        if (choice == 'e'): break #if the choice is end of day, break & print
    managerPrint(totalOrders)

run()