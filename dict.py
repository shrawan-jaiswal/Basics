# # customers = {
# #     "name" : "shrawan jaiswal",
# #     "age" : 25,
# #     "is_verified" : True
# # }

# # print(customers["name"])


# # player = {
# #     "club" : "FC Barcelona",
# #     "country" : "Argentina",
# #     "height" : 175,
    
# # }

# # print(player["height"])
# # print(player.get("country"))

# # #input liyo number
# # phone = input("phone: ")

# # #dictionary
# # digits_mapping = {
# #     "1" : "one",
# #     "2" : "two",
# #     "3" : "three",
# #     "4" : "four"
# # }
# # print(digits_mapping.get("1"))
# # output = ""

# # for charac in phone:
# #     output += digits_mapping.get(charac) + " "
# # print(output)

# #Make a list from the input
# message = input(">")
# words = message.split(' ')
# print(words)

 
# phone = input("phone: ")
# numbers = {
#     "5" : "five",
#     "6" : "six",
#     "7" : "seven",
#     "8" : "eight",
#     "9" : "nine"
# }
# output = ''

# for ch in phone:
#     output += numbers.get(ch, "!") + " "
    
# print(output)

from app import Dice

print(Dice.roll)

