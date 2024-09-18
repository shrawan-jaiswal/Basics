# saree = "red"
# match saree:
#     case "yellow":
#         print("Its yellow")
#     case "pink":
#         print("Its pink")
#     case "blue":
#         print("Match found")
#     case other:
#         print("Match not found")


day = "sunday"
match day:
    case "Sunday":
        print("Today is sunday")
    case "monday":
        print("Today is Monday")
    case _:
        print("Today is nothing")