'''
1.12 Задачи по материалам недели
Задача 7
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм
и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
На вход программе подаётся строка из шести цифр.
Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
'''

x = int(input())
y = x // 1000
z = x % 1000
if (y % 10 + y // 10 % 10 + y // 100 % 10) == (z % 10 + z // 10 % 10 + z // 100 % 10):
    print("Счастливый")
else:
    print("Обычный")

# Форум решений..использется множества
# n = list(map(int, list(input())))
# print('Счастливый' if sum(n[:3]) == sum(n[3:]) else 'Обычный')
