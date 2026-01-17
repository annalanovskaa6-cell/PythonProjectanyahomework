# from statistics import mean
# with open('914.txt') as f:
#     data = [list(map(int, i.split())) for i in f]
# for line in data[::-1]:
#     cnt_3 = [i for i in line if line.count(i) == 3]
#     cnt_1 = [i for i in line if line.count(i) == 1]
#     if len(cnt_3) == 3 and len(cnt_1) == 4 and mean(cnt_1) <= cnt_3[0]:
#         print(sum(line))
#     break            #task 1



# with open('907.txt') as f:
#     data = [list(map(int, i.split())) for i in f]
# def f1(lin):
#     return len(lin) == len(set(lin))
# def f2(arg):
#     arg.sort()
#     return sum(arg[-2:]) <= sum(arg[:-2])
# count = 0
# for line in data:
#     if f1(line) and f2(line):
#         count += 1
# print(count)               #task 2