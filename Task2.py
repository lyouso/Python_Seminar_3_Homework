# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
new_list = []
half_len = round(len(my_list)/2)

if len(my_list)%2 != 0:
    for i in range(half_len+1):
        new_list.append(my_list[i]*my_list[-i - 1])
    print(new_list)
else:
    for i in range(half_len):
        new_list.append(my_list[i]*my_list[-i - 1])
    print(new_list)












# half_len = round(len(my_list)/2)
# print(half_len)

# for i in range(half_len):
#    print(my_list[i]*my_list[(len(my_list)-1)-i])