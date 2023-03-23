# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random


num = input('Введите размер массива: ')
check_num = input('Какое число проверять: ')
flag = True
while flag:
    if num.isdigit() != True:
        num = input('Размер массива указан неверно, введите целое число: ')
    if check_num.isdigit() != True:
        check_num = input('Введите целое число, которое нужно проверить: ')
    else:
        flag = False
num = int(num)
check_num = int(check_num)
mass = [random.randint(1, num+1) for i in range(1, num+1)]
print(f'Получился такой массив {mass}')
min=abs(check_num-mass[0])
print(min)
for i in range(1, len(mass)):
    temp=abs(check_num-mass[i])
    if temp<min:
        min=temp
print(check_num-min)