# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

# Решение №1:

number = 45
result = ''
 
while number > 0:
    result = str(number % 2) + result
    number = number // 2
print(result)

# Решение №2:
number = 45
print(bin(number))