# from timeit import timeit
# nums = list(range(100000))
# code1 = """
# for num in nums:
#     if num % 2 == 0:
#        nums.remove(num)
# """
# code2 = """
# nums = [num for num in nums if num % 2 != 0]
# """
# code3 = """
# nums = list(filter(lambda num: num % 2 == 0, nums))
# """
# program1 = timeit(code1, number = 100, globals = globals())
# program2 = timeit(code2, number = 100, globals = globals())
# program3 = timeit(code3, number = 100, globals = globals())
# print(program1, program2, program3)                               #task 1



# from timeit import timeit
# s = 'a' * 9997 + 'xyz'
# code1 = """
# res = s.endswith('xyz')
# """
# code2 = """
# res2 = s[-3:] == 'xyz'
# """
# program1 = timeit(code1, number = 100, globals = globals())
# program2 = timeit(code2, number = 100, globals = globals())
# print(program1, program2)                                             #task 2



# from timeit import timeit
# textik = "abababdhvbsdbabab"
# code1 = """
# res = textik.count('ab')
# """
# code2 = """
# s = textik.split('ab')
# res2 = len(s) - 1
# """
# code3 = """
# counter = 0
# for x in range(len(textik) -1):
#     if textik[x:x+2] == 'ab':
#         counter += 1
# """
# program1 = timeit(code1, number = 100, globals = globals())
# program2 = timeit(code2, number = 100, globals = globals())
# program3 = timeit(code3, number = 100, globals = globals())
# print(program1, program2, program3)                                      #task 3



# from timeit import timeit
# textik = 'lxosmc'*199995 + 'abcde'
# code1 = """
# res = 'abcde' in textik
# """
# code2 = """
# res2 = textik.find('abcde')
# """
# code3 = """
# s = textik.split()
# res3 = "abcde" in s
# """
# program1 = timeit(code1, number = 100, globals = globals())
# program2 = timeit(code2, number = 100, globals = globals())
# program3 = timeit(code3, number = 100, globals = globals())
# print(program1, program2, program3)                                   #task 4