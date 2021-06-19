# File  : 1365.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-19
# Brief : 중첩 반복문

n = int(input())
a = [[' ']*n for _ in range(n)]

for i in range(n):
    a[0][i] = '*'
    a[i][0] = '*'
    a[i][n-1] = '*'
    a[n-1][i] = '*'
    a[i][i] = '*'
    a[n-1-i][i] = '*'

for i in a:
    for j in i:
        print(j, end='')
    print()
