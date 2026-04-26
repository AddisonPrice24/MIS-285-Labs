soda = "Dr. Pepper $"
sodaprice = 2
tea = "Iced Tea $"
teaprice = 3
wine = "House Wine $"
wineprice = 8
salad = "House Salad $"
saladprice = 7
fries = "Fries $"
fryprice = 5
bread = "Fresh-baked Bread $"
breadprice = 4
burger = "Beef Burger $"
burgerprice = 10
pizza = "Margerita Pizza $"
pizzaprice = 15
pasta = "Chicken Alfredo $"
pastaprice = 15
gelato = "Gelato $"
gelatoprice = 4
tart = "Fruit Tart $"
tartprice = 5
cake = "Chocolate Lava Cake $"
cakeprice = 7
combo1 = "Burger Combo: Beef Burger, Fries, Dr. Pepper $"
combo1price = burgerprice + fryprice + sodaprice
combo2 = "Pizza Combo: Margerita Pizza, Salad, Iced Tea $"
combo2price = pizzaprice + saladprice + teaprice
combo3 = "Pasta Combo: Chicken Alfredo, Bread, Wine $"
combo3price = pastaprice + breadprice + wineprice

#This function displays the menu
def MenuDisplay():
    drinks = soda + str(sodaprice), tea + str(teaprice), wine + str(wineprice),
    appetizers = salad + str(saladprice), fries + str(fryprice), bread + str(breadprice)
    main = burger + str(burgerprice), pizza + str(pizzaprice), pasta + str(pastaprice)
    dessert = gelato + str(gelatoprice), tart + str(tartprice), cake + str(cakeprice)
    combos = combo1 + str(combo1price), combo2 + str(combo2price), combo3 + str(combo3price)
    print("Restaurant Python's Menu")
    print("Beverages: " + str(drinks))
    print("Appetizers: " + str(appetizers))
    print("Main Dish: " + str(main))
    print("Desserts: " + str(dessert))
    print("Combos: " + str(combos))

def IndividualOrder():
    total = 0
    cont = "y"
    while cont == "y":
        order = input("Enter your item: ")
        cont = input("Anything else? y/n: ")
        if order == "Dr. Pepper":
            total += 2
        elif order == "Iced Tea":
            total += 3
        elif order == "House Wine":
            total += 8
        elif order == "House Salad":
            total += 7
        elif order == "Fries":
            total += 5
        elif order == "Fresh-baked Bread":
            total += 4
        elif order == "Beef Burger":
            total += 10
        elif order == "Margerita Pizza":
            total += 15
        elif order == "Chicken Alfredo":
            total += 15
        elif order == "Gelato":
            total += 4
        elif order == "Fruit Tart":
            total += 5
        elif order == "Chocolate Lava Cake":
            total += 7
    print("Your final total is $ " + str(total))

def OrderSystem():
    order = input("Would you like to order a combo? y/n: ")
    if order == "y":
        comboorder = input("What would you like to order?")
        if comboorder == "Burger Combo": 
            print("You've ordered " + str(combo1) + str(combo1price))
        elif comboorder == "Pizza Combo":
            print("You've ordered " + str(combo2) + str(combo2price))
        elif comboorder == "Pasta Combo":
            print("You've ordered " + str(combo3) + str(combo3price))
    else:
        print("What would you like to order? ")
        IndividualOrder()
        
MenuDisplay()
OrderSystem()
