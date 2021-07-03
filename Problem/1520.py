# File : 1520.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-04
# Brief : 2차원 배열

a, b = map(int, input().split())
x, y, z = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(a)]
k = int(input())
dp = [[0]*b for _ in range(a)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def f1(i, j):
    c = 0
    for l in range(8):
        if -1<i+dx[l]<a and -1<j+dy[l]<b:
            c += d[i+dx[l]][j+dy[l]]==1
    return 1 if c==x else 0
def f2(i, j):
    c = 0
    for l in range(8):
        if -1<i+dx[l]<a and -1<j+dy[l]<b:
            c += d[i+dx[l]][j+dy[l]]
    return 1 if y<=c<z else 0
for l in range(k):
    for i in range(a):
        for j in range(b):
            if d[i][j]:
                dp[i][j] = f2(i, j)
            else:
                dp[i][j] = f1(i, j)
    d = dp

for i in d:
    print(*i)
