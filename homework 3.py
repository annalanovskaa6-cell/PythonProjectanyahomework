num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
if num_1 > num_2:
    print(num_1)
else:
    print(num_2)      #task 1



num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
if num_1 > num_2 and num_1 % 2 == 0 and num_1 % 10 != 0:
    print("Первое больше и чётное")
elif num_1 > num_2 and num_1 % 2 != 0:
    print("Первое больше и нечётное ")
elif num_1 > num_2 and num_1 % 10 == 0:
    print ("Первое больше и оканчивается на 0")
elif num_1 < num_2 or num_1 == num_2:
    print(num_2)          #task 2



num_1 = int(input("Введите первое число: "))
num_2 = int(input ("Введите второе число: "))
if num_1 > 0 and num_2 > 0:
    print(num_1 + num_2)
elif num_1 == 0 and num_2 == 0:
    print ("Оба ноль")
else:
    print(num_1 * num_2)      #task 3



num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))
if num_1 < num_2 + num_3 and num_2 < num_1 + num_3 and num_3 < num_1 + num_2:
    print("Треугольник существует")
else:
    print("Треугольник не существует")      #task 4




