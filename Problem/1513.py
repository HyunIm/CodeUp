# File : 1513.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-03
# Brief : 2차원 배열

n = int(input())
a = [[0]*n for _ in range(n)]
i, j, k = n, -1, 1

while n>0:
    for _ in range(n):
        i -= 1
        j += 1
        a[i][j] = k
        k += 1
    n -= 1
    j += 1
    for _ in range(n):
        i += 1
        j -= 1
        a[i][j] = k
        k += 1
    n -= 1
    i += 1

for i in a:
    print(*i)
