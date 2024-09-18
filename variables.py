print("Hello welcome to Network chuck coffee\n")

name = input("What is your name?\n")

if name == "shrawan" or name == "patricia":
    evil_status = input("Are you evil? \n")
    good_deeds = int(input("how many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deeds < 4:
        print("Get out of my cafe you" +name+ "evil")
        exit()
    else:
        print("Hellooo " + name + " thank you so much for coming!!!\n\n\n")

else:
    print("Hello " + name + " thank you so much for coming!!!\n\n\n")

""""
print("Hello " + name + " thank you so much for coming!!!\n\n\n")

menu = "black coffe, milk tea, latte"

print(name + ", What would you like to have? Here is what we are serving.\n" + menu)

order = input()

price = 12

quantity = input("How many coffe would you like to order\n")

total = price * int(quantity)

print("Thank you! Your total is $" + str(total))

print("Sounds good " + name + ", we'll have your " + order + " ready for you in a moment.")

"""