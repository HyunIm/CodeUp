# File : 1493.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-27
# Brief : 2차원 배열

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
s = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        t = 0
        for k in range(j+1):
            t += a[i][k]
        s[i][j] = t + s[i-1][j]

for i in s:
    print(*i)
