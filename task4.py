# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))

if quarter == 1:
    print('I четверть: x > 0, y > 0')
elif quarter == 2:
    print('II четверть: x < 0, y > 0')
elif quarter == 3:
    print('III четверть: x < 0, y < 0')
elif quarter == 4:
    print('IV четверть: x > 0, y < 0')
else:
    print(f'Четверти {quarter} не существует')