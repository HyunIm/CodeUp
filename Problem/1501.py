# File : 1501.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-28
# Brief : 2차원 배열

n = int(input())
for i in range(n):
    for j in range(1, n+1):
        print(n*i+j, end=' ')
    print()
