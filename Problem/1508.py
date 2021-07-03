# File : 1508.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-03
# Brief : 2차원 배열

n = int(input())
a = [[' ']*n for _ in range(n)]
for i in range(n):
    a[i][0] = int(input())

for i in range(1, n):
    for j in range(1, i+1):
        a[i][j] = a[i][j-1] - a[i-1][j-1]

for i in a:
    print(*i)
