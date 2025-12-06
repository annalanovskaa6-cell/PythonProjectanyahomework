# with open ("file.txt", "w", encoding="utf-8") as file:
#     file.write("Привет\nКак дела\n")
# with open ("file.txt", "a", encoding="utf-8") as file:
#     file.write("Как погода\n")
# with open ("file.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     print(lines)          #task 1



# import random
# with open("numbers.txt","w", encoding="utf-8") as file:
#     for _ in range(50):
#         number = random.randint(1,100)
#         file.write(str(number) + "\n")
# with open("numbers.txt","a", encoding="utf-8") as file:
#     for _ in range(20):
#         number = random.randint(1,100)
#         file.write(str(number) + "\n")
# summ = 0
# with open("numbers.txt","r", encoding="utf-8") as file:
#     lines = file.readlines()
#     for line in lines:
#         number = int(line.strip())
#         summ += number
# print(summ)          #task 3