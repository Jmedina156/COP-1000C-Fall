#CIRCLE AREA FUNCTION

radius = int ( input ("Please enter the radius of the circle: "))

def circleArea(radius) :
    area = 3.14159 * radius**2
    return area

value1 = circleArea(radius)

formatted1 = f"{value1:.2f}"

print("The area of the circle is:")
print(formatted1)
print("")


#TAXES FUNCTION

money = int ( input ("Please enter the amount of money: "))
tax = float ( input ("Please enter the tax: "))

def taxesDue (money, tax):
    total = money + (money * tax/100)
    return total

taxes1 = taxesDue (money, tax)

print("The tax is:")
print(format(taxes1, ".2f"))
print ("")


#TEMPERATURE FUNCTION

farenheit = float ( input ("Please enter the temperature in farenheit: "))

def fahrenheitToCelsius (fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

celsiusTemp = fahrenheitToCelsius(farenheit)

formatted1 = f"{celsiusTemp:.4f}"

print("The temperature celsius is:")
print(formatted1)

