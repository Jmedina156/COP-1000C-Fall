#Variables

BASEPRICE = 7.633
EXEEDINGPRICE = 9.259

#Inputs

hours = int(input("Enter the KW hours used: "))

#Computation

if hours <= 1000 :
    amountOwed = hours * BASEPRICE
    amountOwed = amountOwed / 100
    print("Amount owed is $", amountOwed)


elif hours > 1000 :
    amountOwed = 1000 * BASEPRICE + (hours - 1000) * EXEEDINGPRICE
    amountOwed = amountOwed / 100
    print("Amount owed is $", round(amountOwed,7))



