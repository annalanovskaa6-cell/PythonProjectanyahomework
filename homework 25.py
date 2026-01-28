# def make_stats_tracker():
#     numbers = []
#     total_summ = 0
#     def add_number(num):
#         numbers.append(num)
#         total_summ += num
#     def get_average():
#         if not numbers:
#             return 0
#         return total_summ / len(numbers)
#     def get_minimum():
#         if not numbers:
#             return None
#         return min(numbers)
#     def get_maximum():
#         if not numbers:
#             return None
#         return max(numbers)
#     return add_number, get_average, get_minimum, get_maximum
# tracker = make_stats_tracker()
# add_num, avg, min_val, max_val = tracker
# add_num(5)
# add_num(10)
# add_num(3)
# print(avg())
# print(min_val())
# print(max_val())                        #task 1



# def apply_to_each(numbers, operation):
#  return [operation(num) for num in numbers]
# squares = apply_to_each([1, 2, 3, 4, 5], lambda x: x ** 2)
# print("Квадраты чисел:", squares)
# doubles = apply_to_each([1, 2, 3, 4, 5], lambda x: x * 2)
# print("Удвоенные числа:", doubles)                   #task 3