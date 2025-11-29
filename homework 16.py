#def factorial(n):
#     result = 1
#     if n > 1:
#         for i in range(1, n+1):
#             result = result * i
#             return result
#         else:
#             return 'n has to be positive'


# def number_to_digits(number):
#     digits = list(map(int, str(number)))
#     return digits



# from math import sqrt
# def is_prime(n):
#     if n <= 1 or (n % 2 == 0 and n > 2):
#         return False
#     return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))