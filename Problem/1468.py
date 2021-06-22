# File : 1468.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-22
# Brief : 2차원 배열

n = int(input())
for i in range(n):
    if i % 2 == 0:
        for j in range(1, n+1):
            print(i*n+j, end=' ')
    else:
        for j in range(n, 0, -1):
            print(i*n+j, end=' ')
    print()
