# File : 3014.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 데이터 정렬

import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
c = [0] * 100001

for i in a:
    c[i] += 1

for i in range(100001):
    for j in range(c[i]):
        print(i, end=' ')
