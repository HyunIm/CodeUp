# File : 1510.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-03
# Brief : 2차원 배열

n = int(input())
a = [[0]*n for _ in range(n)]
i, j = 0, int(n/2)

for k in range(1, n**2+1):
    a[i][j] = k
    if k%n:
        i = n-1 if i==0 else i-1
        j = 0 if j==n-1 else j+1
    else:
        i = 0 if i==n-1 else i+1

for i in a:
    print(*i)
