'''
1.8 Переменные. Стандартный ввод/вывод
Задача 2
Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна составляет X минут.
Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через X минут после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты.
Помогите Коле определить, на какое время завести будильник.
Часы и минуты в выводе программы должны располагаться на разных строках (см. пример работы программы)
Помните, что для считывания данных нужно вызывать функцию input без аргументов!
Sample Input 1: 480
Sample Output 1:
8
0
Sample Input 2: 512
Sample Output 2:
8
32
'''

X = int(input())
print(X//60)
print(X%60)

# Форум решений
# print(*divmod(int(input()), 60), sep='\n')
