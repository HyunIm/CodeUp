# File : 1502.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-29
# Brief : 2차원 배열

n = int(input())
for i in range(1, n+1):
    for j in range(n):
        print(i+j*n, end=' ')
    print()
