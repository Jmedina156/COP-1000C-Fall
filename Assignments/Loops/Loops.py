def showMenu ():
    print ("")
    print("Taco Palace Menu")
    print ("")
    print("1. Taco - $4.25")
    print("2. Burrito - $5.15")
    print("3. Nachos - $3.00")
    print("4. Soft Drink - $3.75")
    print("5. Quit")

productList = []
total = 0

print ("Welcome to Taco Palace! Please view the menu below and make a selection")
showMenu()

productSelection = int ( input ("Please enter your choice: "))

tacoPrice = 4.25
burritoPrice = 5.15
nachosPrice = 3
softDrinkPrice = 3.75

while productSelection != 5:
    if productSelection == 1:
        productList.append ("Taco")
        total = total + tacoPrice
        print ("You selected a Taco")
    elif productSelection == 2:
        print ("You selected a Burrito")
        productList.append ("Burrito")
        total = total + burritoPrice
    elif productSelection == 3:
        print ("You selected a Nachos")
        productList.append ("Nachos")
        total = total + nachosPrice
    elif productSelection == 4:
        print ("You selected a Soft Drink")
        productList.append ("Soft Drink")
        total = total + softDrinkPrice
    else :
        print ("invalid choice, enter a number from 1 to 5")

    showMenu()
    productSelection = int ( input ("Please enter your choice: "))
    print("")

print ("")
print ("You ordered:")

counter = 0
while counter < len(productList):
    print (productList[counter])
    counter = counter + 1

print ("")

print ("Your total is: $" + format(total, ".2f"))