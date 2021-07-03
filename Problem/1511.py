# File : 1511.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-03
# Brief : 2차원 배열

n = int(input())
a = [i for i in range(1, n+1)]
b = [i for i in range(n*n, n*n-n, -1)]
c = [[i, i+n-1] for i in range(n+1, n*n-n, n)]
print(sum(a+b+sum(c,[])))
