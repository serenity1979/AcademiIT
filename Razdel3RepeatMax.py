'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то,
сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input: abc a bCd bC AbC BC BCD bcd ABC
Sample Output: abc 3
'''
with open('inputT1.txt') as inf:
  with open('outputT1.txt', 'w') as ouf:
    d={}
    for line in inf:
        line = line.strip()
        for key in line.lower().split():
          if key in d:
            d.update({key : d[key]+1})
          else:
            d.setdefault(key,1)
    maxV=max(d.values())
    for key, value in d.items():
      if value==maxV:
        ouf.write(str(key)+' '+str(value)+'\n')
        break
