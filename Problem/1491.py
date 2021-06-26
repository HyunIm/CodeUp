# File : 1491.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-26
# Brief : 2차원 배열

n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
i, j, c, k = n, 0, n*m+1, 1

while n and m:
    for _ in range(n):
        i -= k
        c -= 1
        a[i][j] = c
    m -= 1
    for _ in range(m):
        j += k
        c -= 1
        a[i][j] = c
    n -= 1
    k = -k

for i in a:
    print(*i)
