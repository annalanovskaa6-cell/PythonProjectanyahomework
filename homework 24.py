# def my_filter(func, iter):
#     res = []
#     for item in iter:
#         if func(item):
#             res.append(item)
#     return res
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = my_filter(lambda x: x % 2 == 0, nums)
# print(even)               #hw 1



# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
# res = [x + y for x, y in zip(list1, list2)]
# filtered = [num for num in res if num > 40]
# print(filtered)               #hw 2



# nums = list(range(-10, 11))
# filter = [x for x in nums if abs(x) > 3]
# square = [x**2 for x in filter]
# fin = [x for x in square if x % 10 < 5]
# print(fin[:5])               #hw 3