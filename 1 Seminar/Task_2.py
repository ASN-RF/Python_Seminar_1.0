# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

list = []
max = None
for i in range(5):
    list.append(int(input(f'list[{i}] = ')))
    if list[i] > list[i-1]:
        max = list[i]
print(f'Максимальное число - {max}')
