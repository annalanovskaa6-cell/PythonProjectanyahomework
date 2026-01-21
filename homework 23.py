# students = [("Анна", 16), ("Бронислав", 15), ("Федот", 18)]
# min_student = min(students, key=lambda student: student[1])
# print(f"Человек с минимальным возрастом: {min_student[0]}, возраст: {min_student[1]}")          #task 1



# sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
# nums = [5, -3, 0]
# for num in nums:
#     result = sign(num)
#     print(f"Число {num} - {result}")            #task 2



# add = lambda x, y: x + y
# subtract = lambda x, y: x - y
# def calculator(op1, op2, num1, num2):
#     res_1 = op1(num1, num2)
#     res_2 = op2(num1, num2)
#     return [res_1, res_2]
# result = calculator(add, subtract, 10, 4)
# print(result)               #task 3