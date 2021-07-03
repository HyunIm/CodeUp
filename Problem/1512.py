# File : 1512.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-03
# Brief : 2차원 배열

n = int(input())
x, y = map(int, input().split())
x-=1; y-=1

for i in range(n):
    for j in range(n):
        print((lambda i, j: abs(x-i)+abs(y-j)+1)(i, j), end=' ')
    print()
