'''
2.6 Задачи по материалам недели
Задача 5
Выведите таблицу размером n×n, заполненную числами от 1 до n 2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''

n = int(input())
a = [[0 for m in range(n)] for i in range(n)]
i = 1
j = int(n / 2)
k = int(n / 2)
p = int(n / 2)
for k in range(1, p + 1):
    for j in range(k - 1, n - k + 1):
        a[k - 1][j] = i
        i += 1
    for j in range(k, n - k + 1):
        a[j][n - k] = i
        i += 1
    for j in range(n - k - 1, k - 2, -1):
        a[n - k][j] = i
        i += 1
    for j in range(n - k - 1, k - 1, -1):
        a[j][k - 1] = i
        i += 1
if n % 2 == 1:
    a[p][p] = n * n
for i in range(n):
    for l in range(n):
        print(a[i][l], end=' ')
    print()

# Форум решений
# n = int(input())
# x,y,dx,dy, m = 0,0,0,1, [[0]*n for i in range(n)]
# for i in range(n*n):
#   m[x][y]=str(i+1)
#   if x+dx>=n or x+dx<0 or y+dy>=n or y+dy<0 or m[x+dx][y+dy]:
#       dx,dy = dy,-dx
#   x,y = x+dx, y+dy
# print("\n".join([" ".join(i) for i in m]))
