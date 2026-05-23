# from timeit import timeit
# code1 = """
# s = [x for x in range(10000)]
# """
# code2 = """
# s = []
# for i in range(10000):
#     s.append(i)
# """
# program1 = timeit(code1, number = 10000)
# program2 = timeit(code2, number = 10000)
# print(program2 / program1, program2, program1)                  #task 1



# from timeit import timeit
# s = list(range(10000))
# element = 9999
# code1 = """
# res1 = element in s
# """
# code2 = """
# res2 = s.index(element)
# """
# program1 = timeit(code1, number = 10000, globals = globals())
# program2 = timeit(code2, number = 10000, globals = globals())
# print(program1, program2)                                             #task 2