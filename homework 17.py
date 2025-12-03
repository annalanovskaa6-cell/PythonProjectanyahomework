# def digitize(n):
#     return list(map(int, str(n)))
# print(digitize(10))          #task 1



# import string
# def words_count(text, ignore_case=False, ignore_punctuation=False):
#     count = {}
#     if ignore_case:
#         text = text.lower()
#     if ignore_punctuation:
#         text = text.translate(str.maketrans('', '', string.punctuation))
#     words = text.split()
#     for word in words:
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
#     return count
# print(words_count("Hello World!", ignore_punctuation=True))          #task 2