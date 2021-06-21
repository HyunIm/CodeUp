# File  : 1462.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-21
# Brief : 2차원 배열

n = int(input())
a = [[i+j*n for j in range(n)] for i in range(1, n+1)]

for i in a:
    for j in i:
        print(j, end=' ')
    print()
