#Set the Prices for coffee

name = input("What is your name? \n")

print("Hello " + name + " thank you so much for coming!!!\n")

menu = "black coffe, milk tea, latte"

print(name + ", What would you like to have? Here is what we are serving.\n" + menu)

order = input("Please place your order\n")

if order == "black coffee":
    price = 5
elif order == "milk tea":
    price = 8
elif order == "latte":
    price = 24

else:
    print("we dont have")
    price = 0
    
print(price)