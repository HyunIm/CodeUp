# File  : 1369.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 중첩 반복문

n, k = map(int, input().split())
a = [[' ']*n for _ in range(n)]

for i in range(n):
    a[0][i] = '*'
    a[i][0] = '*'
    a[n-1][i] = '*'
    a[i][n-1] = '*'
    for j in range(n):
        if (i+j)%k==k-1:
            a[i][j] = '*'

for i in a:
    for j in i:
        print(j, end='')
    print()
