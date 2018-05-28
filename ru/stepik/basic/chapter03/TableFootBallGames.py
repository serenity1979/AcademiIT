'''
3.7 Задачи по материалам недели
Задача 1
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит
на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input:3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1

Форум решений
d = {}
for a, p, b, v in (input().split(';') for n in range(int(input()))):
    d[a] = [i + j for i, j in zip(d.setdefault(a, [0, 0, 0, 0, 0]), [1, (p > v), (p == v), (p < v), 3 if p > v else (p == v)])]
    d[b] = [i + j for i, j in zip(d.setdefault(b, [0, 0, 0, 0, 0]), [1, (p < v), (p == v), (p > v), 3 if p < v else (p == v)])]
print(*(i+":" + ' '.join(map(str, d.get(i))) for i in d), sep='\n')

'''


def add_score(key, value):
    if key in d:
        new_score = d[key]
        new_score[0] = new_score[0] + value1[0]
        new_score[1] = new_score[1] + value1[1]
        new_score[2] = new_score[2] + value1[2]
        new_score[3] = new_score[3] + value1[3]
        d.update({key1: new_score})
    else:
        d.setdefault(key1, value1)


n = int(input())
d = {}
for i in range(n):
    score = input().split(';')
    if score[1] == score[3]:
        key1, value1 = score[0], [1, 0, 1, 0]
        key2, value2 = score[2], [1, 0, 1, 0]
    elif int(score[1]) <= int(score[3]):
        key1, value1 = score[0], [1, 0, 0, 1]
        key2, value2 = score[2], [1, 1, 0, 0]
    elif int(score[1]) >= int(score[3]):
        key1, value1 = score[0], [1, 1, 0, 0]
        key2, value2 = score[2], [1, 0, 0, 1]
    add_score(key1, value1)
    add_score(key2, value2)

for key, value in d.items():
    print(key + ':' + str(value[0]), value[1], value[2], value[3], value[1] * 3 + value[2] * 1 + value[3] * 0)
