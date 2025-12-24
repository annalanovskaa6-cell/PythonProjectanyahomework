textik = input("Введите строку: ")
res = ""
for char in textik:
    if char.isupper():
        res += chr(ord(char) + 32)
    else:
        res += char
print(res)