'''
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где 
mod — это взятие остатка от деления, 
pow — возведение в степень, 
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
'''

a, b, o = float(input()), float(input()), input()
if o=="+":
  print(a+b)
elif o=="-":
  print(a-b)
elif o=="*":
  print(a*b)
elif o=="/":
  if b==0:
    print('Деление на 0!')
  else:
    print(a/b)
elif o=="mod":
  if b==0:
    print('Деление на 0!')
  else:
    print(a%b)
elif o=="pow":
  print(a**b)
elif o=="div":
  if b==0:
    print('Деление на 0!')
  else:
    print(a//b)
