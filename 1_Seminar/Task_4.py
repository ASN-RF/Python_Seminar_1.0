# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3
# 1 вариант
# a = float(input())
# a = a % 1
# a = (a*10)
# print(round(a))
# 2 вариант
from math import trunc


a = float(input())
a = trunc(a%1 * 10)
print(round(a))

# 3 вариант
# N = float(input('Введите число: '))
# x = int((N - int(N))*10)
# print(f'{N} -> ', end='')
# if x <= 0:
#     print('нет')
# else:
#     print(x)