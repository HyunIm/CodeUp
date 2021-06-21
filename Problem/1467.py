# File  : 1467.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-21
# Brief : 2차원 배열

n, m = map(int, input().split())
a = [[i+j*n for j in range(m-1, -1, -1)] for i in range(1, n+1)]

for i in a:
    for j in i:
        print(j, end=' ')
    print()
