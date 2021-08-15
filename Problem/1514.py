# File : 1514.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-15
# Brief : 기초

def f(x, y):
    for i in range(7):
        if a[x][i] == 2: a[x][i] = 1; f(x, i)
        elif a[i][y] == 2: a[i][y] = 1; f(i, y)
        a[x][i] = 1; a[i][y] = 1
s = [list(map(int, input().split())) for _ in range(3)]
a = [[0]*7 for _ in range(7)]
for x, y in s: a[x-1][y-1] = 2
for i in range(7):
    if a[3][i] == 2: a[3][i] = 1; f(3, i)
    a[3][i] = 1
for x, y in s: a[x-1][y-1] = 2
for i in a: print(*i)
