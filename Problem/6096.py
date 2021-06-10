# File : 6096.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-10
# Brief : 종합

d = [0] * 19
for i in range(19):
    d[i] = list(map(int, input().split()))

n  = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    for j in range(19):
        d[x][j] = 0 if d[x][j] == 1 else 1
        d[j][y] = 0 if d[j][y] == 1 else 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()
