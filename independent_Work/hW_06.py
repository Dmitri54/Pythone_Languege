# 6. Напишу программу, которая на вход принимает число и выдаёт, 
# является ли число чётным (делится ли оно на два без остатка).
# 4 -> да
# -3 -> нет
# 7 -> нет
# ========================================================================================================

print('Эта программа принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка')
num = int(input('Введите число и нажмите Enter: '))

if num %2 == 0:
    print(f'Да, число {num} является чётным.')
else:
    print(f'Нет, число {num} НЕ является чётным.')

