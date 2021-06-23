# File : 1476.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-23
# Brief : 2차원 배열

n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
c = 1

for k in range(0, n+m-1):
    for i in range(m):
        for j in range(n):
            if i+j == k:
                a[j][i] = c
                c += 1

for i in a:
    print(*i)
