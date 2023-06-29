# rating system or something

my_rating_list = [9, 6, 4, 4, 3]

new_user_number = input("What number do you want to add?: ")
new_user_number = int(new_user_number) #convers user_number into integer.

index = 0
while index < len(my_rating_list) and new_user_number < my_rating_list[index]:
    index += 1

my_rating_list.insert(index, new_user_number)

print(my_rating_list)