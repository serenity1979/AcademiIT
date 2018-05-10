
"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end

Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end
Sample Output 2:
4

"""
# my variant
'''
s1="st"
a=[]
b=[]
j=0
while s1!="end":
    s1=input()
    if s1=="end":
        break
    else:
        a=[int(i) for i in s1.split()]
        l=len(a)
        b.append(a)
        j+=1
for m in range(j):
    for n in range(l):
        s=0
        if m-1<0:
            s+=b[j-1][n]
        else:
            s+=b[m-1][n]
        if m+1>=j:
            s+=b[0][n]
        else:
            s+=b[m+1][n]
        if n-1<0:
            s+=b[m][l-1]
        else:
            s+=b[m][n-1]
        if n+1>=l:
            s+=b[m][0]
        else:
            s+=b[m][n+1]
        print(s, end=' ')
    print()
'''

# optimalno
c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()
