'''
3.4 Файловый ввод/вывод
Задача 1
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется
ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных.
Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.
Sample Input: a3b4c2e10b1
Sample Output: aaabbbbcceeeeeeeeeeb
'''
with open('input.txt') as inf:
    with open('output.txt', 'w') as ouf:
        for line in inf:
            line = line.strip()
            l, n, lengStr = '', 0, len(line)
            s = ''
            for i in range(lengStr):
                if line[i].isdigit():
                    n = n * 10 + int(line[i])
                else:
                    l += line[i]
                if i + 1 == lengStr or line[i + 1].isalpha():
                    s = s + l * n
                    l, n = '', 0
            ouf.write(s + '\n')
