# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех
# значений предикат.
x = int(input('ведите первое число: '))
y = int(input('введите второе число: '))
z = int(input('введите третье число: '))

print(not(x or y or z) == (not x) and (not y) and (not z))