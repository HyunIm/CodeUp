# File : 1362.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-10
# Brief : 기초

n = int(input())
c = int(n*(n+1)/2)
for i in range(1, n+1):
    for j in range(i):
        print(c, end=' ')
        c -= 1
    print()
