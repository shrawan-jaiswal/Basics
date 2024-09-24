LeoMessi = {
    "Intermiami" : {
        "Jersey_no" : 10,
        "Coach" : "Tata Martino",
        "Color" : "Pink",
    },
    "PSG" : {
        "Jersey_no" : 30,
        "Coach" : "Ernesto Valverde",
        "Color" : "Blue",
    },
}

for club, details in LeoMessi.items():
    print(f"\nClub:{club}")
    Jersey = f"{details["Jersey_no"]}"
    Manager = f"{details["Coach"]}"
    Color = f"{details["Color"]}"

    print(f"Jersey_no: {Jersey}")
    print(f"Manager: {Manager}")
    print(f"Color: {Color}")
    
prompt = "If you share your name, we can personalizze the messages you see."
prompt += "\n What is your first name?"
name = input(prompt)
print(f"\n Hello {name}")

height = input("How tall are you in cm?: ")
height = int(height)

if height >= 170:
    print("Perfect height!!!")
else:
    print("Short height!!!")

number = input("tell me a number to verify odd or even?: ")
number = int(number)

if number % 2 == 0:
    print(f"\n the number  {number} is even")

else:
    print(f"\n the number {number} is odd")

current_number = 1
while current_number <= 15:
    print(current_number)
    current_number += 1

prompt = "\n Tell me something, and I will repeat it back to you"
prompt += "\n Enter quit to end the program: "

message = ""
while message != "quit":
    message = input(prompt)
    print(message)

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)
    # print(set1)

for i in range(3, 9):
    set2.add(i)
    # print(set2)

set3 = set1.intersection(set2)
print(set3)

set4 = set1 | set2
print(set4)


def greet(first_name, last_name, club):  # This is parameters
    print(f"Hello {first_name} {last_name}")
    print(f"Welcome to Club {club} ")
    

greet("Shrawan", "Jaiyswal" , "Barcelona")    #This is arguments
greet("Dipisha", "Guiday", "Inter Miami")


def greeting(firstname):
    return f"Hello {firstname}"

leo = (greeting("Shrawan"))
print(leo)

#Example of Recursion
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)


show(3)
        