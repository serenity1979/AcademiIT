'''
3.7 Задачи по материалам недели
Задача 3
Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте
ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное. Напишем подобную систему.
Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей в списке известных слов,
после передаётся  d строк с одним словарным словом на строку, затем — количество l строк текста, после чего — l строк текста.
Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается.
Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.
Sample Input:3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa
Sample Output:
aab
aba
c
aaa

Форум решений

dic = {input().lower() for i in range(int(input()))}
wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}
print(*wrd.difference(dic), sep="\n")
'''
n = int(input())
mydict = set()
for i in range(n):
    mydict.add(str(input()).lower())

l = int(input())
mytext = set()
for i in range(l):
    line = set(str(input()).lower().split())
    mytext.update(line)
newword = mytext.difference(mydict)
for word in newword:
    print(word)
