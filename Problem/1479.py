# File : 1479.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-25
# Brief : 2차원 배열

n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
c = 1

for k in range(-m, n):
    for i in range(n-1, -1, -1):
        for j in range(m):
            if i-j == k:
                a[i][j] = c
                c += 1

for i in a:
    print(*i)
