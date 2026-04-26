print("Welcome to the Oregon Tech Basketball Event Ticketing System.")
regular = 25
guest = 20
vip = 15
ticketprice = 0
totalticketprice = 0
ticketcount = 0
cont = "y"
while cont == "y":
    tickettype = input("Enter attendee type (student/parent/guest/regular/vip/staff): ")
    if tickettype == "cancel":
        break
    if tickettype == "parent" or tickettype == "regular":
        ticketprice = regular
        print("Ticket price: $" + str(ticketprice))
        ticketcount += 1
        if tickettype == "parent":
            print("Discount applied: 5%")
            discountamount = ticketprice * 0.05
            discountedprice = ticketprice - discountamount
            print("Final Ticket Price: $" + str(discountedprice))
            cont = input("Anything else? y/n: ")
            print("Add another ticket? (y/n): " + str(cont))
            totalticketprice += discountedprice
    elif tickettype == "guest" or tickettype == "student" or tickettype == "staff":
        ticketprice = guest
        print("Ticket price: $" + str(ticketprice))
        ticketcount += 1
        if tickettype == "student" or tickettype == "staff":
            print("Discount applied: 10%")
            discountamount = ticketprice * 0.1
            discountedprice = ticketprice - discountamount
            print("Final Ticket Price: $" + str(discountedprice))
            cont = input("Anything else? y/n: ")
            print("Add another ticket? (y/n): " + str(cont))
            totalticketprice += discountedprice
    elif tickettype == "vip": 
        ticketprice = vip
        print("Ticket price: $" + str(ticketprice))
        cont = input("Anything else? y/n: ")
        print("Add another ticket? (y/n): " + str(cont))
        totalticketprice += ticketprice
        ticketcount += 1
    else:
        print("Invalid ticket type. Please try again.")
        cont = "y"
    if totalticketprice >= 100:
        print("Your total exceeds $100.")
        break

purchaseswag = input("Would you like to purchase swag? (y/n): ")
swagtotal = 0
print("Would you like to purchase swag? (y/n): " + str(purchaseswag))
if purchaseswag == "y":
    print("Avalible Swag: ")
    print("T-Shirt: $15")
    print("Cap: $10")
    print("Hoodie: $30")
    print("Mug: $8")
    print("Sticker Pack: $5")
    print("Enter skip to finish.")
    item = input("Enter Swag Item: ")
    print("Enter Swag Item: " + item)
    while item != "skip": 
        if item == "tshirt":
            swagtotal += 15
            print("Added: T-shirt $15")
            item = input("Enter Swag Item: ")
        elif item == "cap":
            swagtotal += 10
            print("Added: Cap $10")
            item = input("Enter Swag Item: ")
        elif item == "hoodie":
            swagtotal += 30
            print("Added: Hoodie $30")
            item = input("Enter Swag Item: ")
        elif item == "mug":
            print("Added: Mug $8")
            swagtotal += 8
            item = input("Enter Swag Item: ")
        elif item == "stickers":
            print("Added: Sticker Pack $5")
            swagtotal += 5
            item = input("Enter Swag Item: ")
totalcost = totalticketprice + swagtotal
print("Final Summary: ")
print("Total Tickets Purchased: " + str(ticketcount))
print("Total Ticket Cost: " + str(totalticketprice))
print("Total Swag Cost: " + str(swagtotal))
print("Grand Total: " + str(totalcost))
