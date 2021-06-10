# File : 6095.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-10
# Brief : 종합

n = int(input())
d = [[0] * 20 for i in range(20)]

for _ in range(n):
    i, j = map(int, input().split())
    d[i][j] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
