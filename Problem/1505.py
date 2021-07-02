# File : 1505.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-03
# Brief : 2차원 배열

n = int(input())
a = [[0]*n for _ in range(n)]
i, j, c, k = 0, -1, 0, 1

while n:
    for _ in range(n):
        j += k
        c += 1
        a[i][j] = c
    n -= 1
    for _ in range(n):
        i += k
        c += 1
        a[i][j] = c
    k = -k

for i in a:
    print(*i)
