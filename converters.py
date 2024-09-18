# weight = int(input("Enter your weight: "))
# unit = input("(L)bs or (k)gs\n")

# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(f"you are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"you are {converted} pounds")

def lb_to_kg(weight):
    return weight * 0.45

def kg_to_lb(weight):
    return weight / 0.45

