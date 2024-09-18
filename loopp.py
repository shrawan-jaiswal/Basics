# i = 10
# while i >= 2:
#     print("*" *  i)
#     i = i - 2
    
# print("done")

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count +=1
    if guess == secret_number:
        print("you won!")
        break

else:
    print("You lose!")


# lottery = 5
# count = 0
# limit = 4

# while count < limit:
#     guess = int(input("guess: "))
#     count += 1
#     if guess == lottery:
#         print("you won")
#         exit()
    
