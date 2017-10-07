"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
"""

x=int(input())
y=int(input())
z=int(input())
if x>=y:
   if z>=x:
     print(z)
     print(y)
     print(x)
   elif z>y:
     print(x)
     print(y)
     print(z)
   else:
     print(x)
     print(z)
     print(y)
else:
   if z>=y:
     print(z)
     print(x)
     print(y)
   elif z>x:
     print(y)
     print(x)
     print(z)
   else:
     print(y)
     print(z)
     print(x)
