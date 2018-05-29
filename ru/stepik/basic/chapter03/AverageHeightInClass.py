'''
3.7 Задачи по материалам недели
Задача 5
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля: Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно.
В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить
значение в виде вещественного числа. Выводить информацию о среднем росте следует в порядке возрастания номера класса
(для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк, например:
Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153
Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0

'''
d = {a: [0, 0] for a in range(1, 12)}
s = []
with open('shcool.txt') as inf:
    for line in inf:
        key, name, height = line.strip().split()
        if int(key) in d:
            s = d.get(int(key))
            s[0] += 1
            s[1] += int(height)
            d.update({int(key): s})

for key, value in d.items():
    if value[0] == 0:
        print(str(key) + ' -')
    else:
        print(str(key) + ' ' + str(value[1] / value[0]) )