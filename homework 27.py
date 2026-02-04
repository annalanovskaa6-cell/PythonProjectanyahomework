# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
# result = power(2, 3)
# print(result)                     #task 1



# def summa(n):
#     n = abs(n)
#     if n < 10:
#         return n
#     else:
#         return (n % 10) + summa(n // 10)
# num = 123
# result = summa(num)
# print(f"Сумма цифр числа {num} равна: {result}")                         #task 2



# def maxik(list):
#     if len(list) == 1:
#         return list
#     else:
#         max_of_rest = maxik(list[1:])
#         return list if list > max_of_rest else max_of_rest
# nums = [3, 5, 2, 8, 9]
# print(maxik(nums))                         #task 3