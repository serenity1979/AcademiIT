
"""
Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, которая выводит все позиции, на которых встречается число x в переданном списке lst.
Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

"""
lst1=[int(i) for i in input().split()]
x=int(input())
cnt=0
n=len(lst1)
for i in range(0,n):
    if lst1[i]==x:
        cnt+=1
        print(i, end=' ')
if cnt==0:
    print('Отсутствует')
