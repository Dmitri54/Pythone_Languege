# Задача: предложить улучшения кода для уже решённых задач (3-5 задач):
# С помощью использования: lambda, filter, map, zip, enumerate, list comprehension.
# -------------------------------------------------------------------------------------------------
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11
# ==================================================================================================

number = input('Введите число: ').split('.')
print(sum(map(int, number[1])))