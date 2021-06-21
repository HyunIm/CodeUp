# File  : 1463.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-21
# Brief : 2차원 배열

n = int(input())
a = [[i+j*n for j in range(n)] for i in range(n, 0, -1)]

for i in a:
    for j in i:
        print(j, end=' ')
    print()
