'''
1.12 Задачи по материалам недели
Задача 4
Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые.
Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
которая бы выводила площадь получившейся комнаты. Для числа ? в стране Малевии используют значение 3.14.

Формат ввода, который используют Малевийцы:
треугольник
a
b
c
где a, b и c — длины сторон треугольника

прямоугольник
a
b

где a и b — длины сторон прямоугольника

круг
r
где r — радиус окружности
'''
x = input()
if x == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif x == 'прямоугольник':
    a, b = float(input()), float(input())
    print(a * b)
elif x == 'круг':
    r = float(input())
    print(3.14 * r ** 2)
else:
    print('??')