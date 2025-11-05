# def validate_username(username):
#     if not username.startswith('@'):
#         return False
#     if not (4 <= len(username) <= 16):
#         return False
#     for char in username[1:]:
#         if not (char.isalnum() or char == '_'):
#             return False
#     return True
# user = input("Введите имя пользователя: ")
# if validate_username(user):
#     print("Принято!")
# else:
#     print("Имя пользователя не подходит")        #task 1



import random
my_list = [random.randint(1, 100)for _ in range(5)]
print("Исходный список: ", my_list)

minimum = my_list[0]
maximum = my_list[0]
for number in my_list[1:]:
    if number < minimum:
        min_val = number
    if number > maximum:
        max_val = number
print("Минимум: ", minimum)
print("Максимум: ", maximum)           #task 2