# File : 1504.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-01
# Brief : 2차원 배열

n = int(input())
for i in range(1, n+1):
    for j in range(n):
        print(n-i+j*n+1 if j%2 else i+j*n, end=' ')
    print()
