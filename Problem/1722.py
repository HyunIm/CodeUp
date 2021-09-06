# File : 1722.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-06
# Brief : 기초

import math
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
r = 0
for i in range(1, n):
    r += math.sqrt(abs(a[i-1][0]-a[i][0])**2 + abs(a[i-1][1]-a[i][1])**2)
print('%.2f'%r)
