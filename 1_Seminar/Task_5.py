# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
x = int(input('Здравствуйте!\nВведите Ваше любимое число:\n'))
if x % 5 == 0 and x % 10 == 0 and x % 15 == 0 and x % 30 != 0:
    print ('Да, Ваше любимое число кратно 5 и 10, и даже 15, но не кратно 30')
elif x % 5 == 0 and x % 10 == 0 and x % 15 == 0 and x % 30 == 0:
    print ('НЕТ, Ваше любимое число кратно 5 и 10, и даже 15 и 30')
elif x % 5 == 0 and x % 10 == 0 and x % 30 != 0:
    print ('Да, Ваше любимое число кратно 5 и 10, но не кратно 15 и 30')
elif x % 15 == 0 and x % 30 != 0:
    print ('Да, Ваше любимое число кратно 5 и 15, но не кратно 10 и 30')
elif x % 15 == 0 and x % 30 != 0:
    print ('Да, Ваше любимое число кратно 5 и 15, но не кратно 10 и 30')    
elif x % 5 == 0 and x % 10 != 0 and x % 15 != 0 and x % 30 != 0:
    print ('Нет, Ваше любимое число только кратно 5, но не кратно 10, 15 и 30')    
else:
    print ('Нет, Ваше любимое число НЕ кратно ни 5, ни 10, ни 15, ни 30')


