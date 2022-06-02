# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


my_list = [1.1, 1.2, 3.1, 5, 10.01]
min = my_list[0] - int(my_list[0])
max = my_list[1] - int(my_list[1])

for i in my_list:
    frac = i - int(i)
    if frac < min and frac !=0:
         min = frac
    elif frac > max:
        max = frac
print(f'Минимальное значение равно {round(min, 2)}')
print(f'Максимальное значение равно {round(max, 2)}')
diff = max - min
print(round(diff, 2))





