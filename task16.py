# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

import random


num = input('Введите размер массива: ')
search_num = input('Какое число искать: ')
flag = True
while flag:
    if num.isdigit() != True:
        num = input('Размер массива указан неверно, введите целое число: ')
    if search_num.isdigit() != True:
        search_num = input('Введите целое число, которое нужно искать: ')
    else:
        flag = False
num = int(num)
search_num = int(search_num)
mass = [random.randint(1,num//2) for i in range(1, num+1)]
print(f'Получился такой массив {mass}')
counter=0
for i in range(len(mass)):
    if mass[i]==search_num:
        counter+=1
print(f'Число {search_num} в массиве повторяется {counter} раз')




