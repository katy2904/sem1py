# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
# ними в 2D пространстве.

print('Введите координаты X и Y первой точки:')
x1, y1 = int(input()), int(input())

print('Введите координаты X и Y второй точки:')
x2, y2 = int(input()), int(input())

print(f'Расстояние между точками ({x1}, {y1}) и ({x2}, {y2}) равно '
      f'{round(((x1-x2)**2 + (y1-y2)**2)**0.5, 2)}')