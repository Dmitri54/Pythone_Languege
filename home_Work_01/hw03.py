# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x = 34; y = -30 -> 4
# - x = 2; y = 4-> 1
# - x = -34; y = -30 -> 3
# ------------------------------------------------------------------------------------------------

print('Программа принимает на вход координаты точки (X и Y), \nпричём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, \nв которой находится эта точка')
def inputCoordinates(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        a.append(float(input(f"Введите значение {xy[i]}: ")))
    return a

def checkCoordinates(xy):
    if xy[0] > 0 and xy[1] > 0:
        print(f'Точка находится в 1 четверти плоскости')
    elif xy[0] < 0 and xy[1] > 0:
        print(f'Точка находится в 2 четверти плоскости')
    elif xy[0] < 0 and xy[1] < 0:
        print(f'Точка находится в 3 четверти плоскости')
    elif xy[0] > 0 and xy[1] < 0:
        print(f'Точка находится в 4 четверти плоскости')
    elif xy[0] == 0 or xy[1] == 0:
        print(f'Введены не корректные данные. Значения X или Y не должны равняться нулю.')


coordinates = inputCoordinates(2)
checkCoordinates(coordinates)

