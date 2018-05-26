'''
3.1 Функции
Задача 2
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]
lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации.
'''


def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l.insert(i + 1, int(l[i] / 2))
        l.pop(i)


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)  # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)  # [5, 4]

lst = [5]
modify_list(lst)
print(lst)  # []

# Форум решений
# def modify_list(l):
#    l[:] = [i//2 for i in l if not i % 2]
