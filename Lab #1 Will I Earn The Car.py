#Lab 1: Will I Earn The Car?
def TestScorePercentageCalculator():
    score1 = int(input("Enter Test Score #1"))
    score2 = int(input("Enter Test Score #2"))
    score3 = int(input("Enter Test Score #3"))
    averagescore = str(((score1 + score2 + score3)/300)*100)
    print ("Test Score #1: " + str(score1))
    print ("Test Score #2: " + str(score2))
    print ("Test Score #3: " + str(score3))
    print ("Overall Percentage: " + averagescore + "%")

def CarPaymentCalculator():
    msrp = int(input("Enter MSRP: "))
    apr = int(input("Enter APR: "))
    months = int(input("Enter the number of months to pay: "))
    monthlyinterestrate = (apr / 12 / 100)
    monthlypayment = float((msrp * (monthlyinterestrate * (1 + monthlyinterestrate) ** months) / ((1 + monthlyinterestrate) ** months - 1)))
    totalpaid = float(monthlypayment * months)
    roundedtotalpaid = round(totalpaid, 2)
    interestpaid = float(totalpaid - msrp)
    roundedinterestpaid = round(interestpaid, 2)
    print ("I would like to buy a car with a MSRP of $" + str(msrp))
    print ("Without tax, the total cost of the car is $" + str(roundedtotalpaid))
    print ("The total interest paid is $" + str(roundedinterestpaid))

def DownPaymentSavingsCalculator():
    balance = 0
    months = 0
    monthlydeposit = 200
    monthlyinterestrate = 0.04
    monthlysavings = monthlydeposit
    while balance < 5000:
        balance += monthlysavings + (balance * monthlyinterestrate)
        months += 1
        totalsavings = (monthlysavings * months) * (1 + monthlyinterestrate)
    print("To save my $5000 down payment by depositing $200/month at a 4% interest rate, it will take " + str(months) + " months and the final balance will be " + str(totalsavings))

def SalesTaxCalculator():
    msrp = int(input("Enter MSRP: "))
    salestaxrate = int(input("Enter Sales Tax Rate: "))
    apr = int(input("Enter APR: "))
    months = int(input("Enter the number of months to pay: "))
    monthlyinterestrate = (apr / 12 / 100)
    monthlypayment = float((msrp * (monthlyinterestrate * (1 + monthlyinterestrate) ** months) / ((1 + monthlyinterestrate) ** months - 1)))
    totalpaid = float(monthlypayment * months)
    interestpaid = float(totalpaid - msrp)
    finaltotalpaid = float(totalpaid + interestpaid)
    #this is where the sales tax is brought in
    salestax = float(finaltotalpaid * (salestaxrate / 100))
    finaltaxedprice = float(finaltotalpaid + salestax)
    taxedmonthlypayment = float((finaltaxedprice * (monthlyinterestrate * (1 + monthlyinterestrate) ** months) / ((1 + monthlyinterestrate) ** months - 1)))
    roundedtaxedmonthlypayment = round(taxedmonthlypayment, 2)
    taxedtotalinterstpaid = float(taxedmonthlypayment - finaltaxedprice)
    finaltotalcost = float(taxedmonthlypayment * months)
    roundedfinaltotalcost = round(finaltotalcost, 2)
    print ("With sales tax added, my monthly payment would be $"  + str(roundedtaxedmonthlypayment))
    print ("With sales tax added, the total cost of the car is $" + str(roundedfinaltotalcost))

def FinalPrint():
    TestScorePercentageCalculator()
    CarPaymentCalculator()
    DownPaymentSavingsCalculator()
    SalesTaxCalculator()

FinalPrint()