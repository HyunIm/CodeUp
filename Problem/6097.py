# File : 6097.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-10
# Brief : 종합

h, w = map(int, input().split())    # 세로(h), 가로(w)
n = int(input())    # 막대의 개수
s = [0] * n
for i in range(n):
    s[i] = list(map(int, input().split()))
a = [[0] * w for _ in range(h)] # 격자판

for i in range(n):
    l = s[i][0] # 막대의 길이
    d = s[i][1] # 막대의 방향
    x = s[i][2] - 1 # x좌표
    y = s[i][3] - 1 # y좌표
    for j in range(l):
        if d == 0:
            a[x][y + j] = 1
        else:
            a[x + j][y] = 1

for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()
