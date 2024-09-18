# # camping_list = ["sleeping bag", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallow"]
# # print(type(camping_list))
# # me = camping_list[0]
# # print(me)


# # camp_site = ["crystal lake", 404, 89.3, True]
# # #print the last element of the list

# # last_item = camp_site[-1]
# # print(last_item)

# # # To print item from last it starts from -1 -2 and so on.


# # #camping_list.extend(["toilet paper", "Snickers", "123.com"])
# # #camping_list.insert(0, "Dipisha")
# # #camping_list.insert(-1, "health")
# # camping_list.remove("sleeping bag")

# # camping_list.pop(0)
# # print(camping_list)


# # atuple = ("shrawan", "jaiyswal", 99)
# # atuple[0] = ("jaiswal")


# numbers = [25, 2, 6, 10, 13, 60, -1, 60, 60, 60]
# print(25 in numbers)
# # print(numbers.index(6))
# number2 = numbers.copy()
# numbers.append(12)
# print(number2)
# print("this is that\n")
# numbers.sort()
# numbers.reverse()
# print(numbers)

# print(numbers.count(60))
# max = numbers[0]
# min = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number

# print(max)

# for number in numbers:
#     if number < min:
#         min = number
# print(min)

# numbers = [2, 2, 6, 3, 6, 7, 9, 7, 8, 10, 2]
# clean = []
# for number in numbers:
#     if number not in clean:
#         clean.append(number)
# print(clean)


numbers = [6, 3, 6, 7, 9, 7, 8, 10, 2, 9, 9, 8]

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
uniques.sort()
print(uniques)