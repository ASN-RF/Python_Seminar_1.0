# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# x = int(input('Здравствуйте!\nВведите Ваше любимое число:\n'))
# y = -x
# print(f'{x} ->', end=" ")
# while y < x:
#     print(f'{y},', end=" ")
#     y = y+1
# if y == x:
#     print(f'{y}.', end=" ")
x = int(input('Здравствуйте!\nВведите Ваше любимое число:\n'))
print(f'{x} ->', end=" ")
for i in range(-x, x+1):
    print(f'{i},', end=" ")