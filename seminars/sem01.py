#  Урок 1. Семинар. Знакомство с языком Python.
# --------------------------------------------------------------------------------------------
# Задача 1. Напишу программу, которая принемает на вход два числа и проверяет,
# является ли одно число квадратом другого.
# --------------------------------------------------------------------------------------------

# num_1 = int(input('Введите число 1: '))
# num_2 = int(input('Введите число 2: '))
# if (num_2 == (num_1 ** 2)) or (num_1 == (num_2 ** 2)): # В данном случае можно за место or написать and.
#     print(True)
# else:
#     print(False)
# ---------------------------------------------------------------------------------------------
# Задача 2. Напишу программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Пример:
# -1, 4, 8, 7, 5 -> 8
# -78, 55, 36, 90, 2 -> 90
# ---------------------------------------------------------------------------------------------
# 1. Решение (через условие):
# num_1 = int(input('Введите число 1: '))
# num_2 = int(input('Введите число 2: '))
# num_3 = int(input('Введите число 3: '))
# num_4 = int(input('Введите число 4: '))
# num_5 = int(input('Введите число 5: '))
# max = num_1
# if max < num_2:
#     max = num_2
# if max < num_3:
#     max = num_3
# if max < num_4:
#     max = num_4
# if max < num_5:
#     max = num_5
# print(max)
# -----------------------------------------------------------------------------------------------
# 2. Решение (через цикл):
# a = [-1, 4, 8, 7, 5]
# max_num = 0
# for b in a:
#     if b > max_num:
#         max_num = b
# print(max_num)
# --------------------------------------------------------------------------------------------
# 3. Решение (список, цикл) Препод:
# my_list = [] # Создал список.
# my_list.append(20) # append() - добавит элемент в конец списка.
# my_list.append(21)
# my_list.append(22)

# range(5) -> [0, 1, 2, 3, 4]
# range(5, 16) -> [5, 6, 7,.., 14, 15, 16]
# range(1, 11, 2) -> [1, 3, 5, 7, 9, 11]

# for i in range(5): # Заполнил список элементами. 
#     num = int(input('--> ')) # Ввод элемента с клавиатуры.
#     my_list.append(num)
# print(my_list)

# my_list = [-1, 4, 8, 7, 5]
# # print(max(my_list)) # Выстроенная функция нахождения максимального число.
# num_max = my_list[0]
# # for iten in my_list:
# for iten in my_list[1:]: # Чтобы непроверять my_list[0] самим с собой, использую СРЕЗЫ [1:] - со второго элем. до конца.
#     if iten > num_max:
#         num_max = iten
# print(num_max)

# my_list = [-1, 4, 8, 7, 5]
# print(my_list[1:3]) # СРЕЗ 
# print(my_list[::2]) # С шагом 2
# -------------------------------------------------------------------------------------------------
# 4. Решение (список, цикл, поиск по индексу):
# my_list = [-1, 4, 8, 7, 5]
# num_max = my_list[0]
# num_max_i = 0
# for i in range(1, len(my_list)): # Пишу, range - чтобы пройти по индексам и запомнить индекс максимального числа.
#     if my_list[i] > num_max:
#         num_max = my_list[i]
#         num_max_i = i
# print(num_max, num_max_i)
# --------------------------------------------------------------------------------------------
# Задача 3. Напишу программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# --------------------------------------------------------------------------------------------
# РЕШЕНИЕ:
# input('Программа выводит числа от -N до N.')
# num = int(input('Введите число и нажмите Enter: '))
# for i in range(-num, num):
#     print(i, end = ", ")
# print(num)
# --------------------------------------------------------------------------------------------------
# Задача 4. Напишу программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
# ----------------------------------------------------------------------------------------------------
# РЕШЕНИЕ 1:
# number = input('Введите дробное число: ') # 345,123
# print(number.split(',')[1][0]) # Делю строку по запятой, обращаюсь ко второй половине = 123, к первому элементу строки = 1.
# --------------------------------------------------------------------------------------------------
# РЕШЕНИЕ 2:
# number = float(input('Введите дробное число: '))
# number *= 10
# # print(number)
# number = int(number)
# # print(number)
# print(number % 10)
# -------------------------------------------------------------------------------------------------
# Задача 5. Напишу программу, которая принимает на вход число и проверяет, 
# кратно ли оно (5 и 10) или (15, но не 30)
# --------------------------------------------------------------------------------
# РЕШЕНИЕ:
# num = int(input("Введите число: "))
# if (num % 5 == 0) and (num % 10 == 0) or (num % 15 == 0) and (num % 30 != 0):
#     print('Да')
# else:
#     print('Нет')


