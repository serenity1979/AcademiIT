"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
"""

x,y,z=int(input()),int(input()),int(input())
if x>=y:
   if z>=x:
     print(z,'\n',y,'\n',x)
   elif z>y:
     print(x,'\n',y,'\n',z)
   else:
     print(x,'\n',z,'\n',y)
else:
   if z>=y:
     print(z,'\n',x,'\n',y)
   elif z>x:
     print(y,'\n',x,'\n',z)
   else:
     print(y,'\n',z,'\n',x)
