'''
3.4 Файловый ввод/вывод
Задача 3
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667

'''
bm, bf, blr, n = 0, 0, 0, 0
with open('inputT2.txt') as inf:
    with open('outputT2.txt', 'w') as ouf:
        for line in inf:
            s = line.split(';')
            bm += int(s[1])
            bf += int(s[2])
            blr += int(s[3])
            n += 1
            ouf.write(str((int(s[1]) + int(s[2]) + int(s[3])) / 3) + '\n')
        ouf.write(str(bm / n) + ' ' + str(bf / n) + ' ' + str(blr / n) + '\n')
