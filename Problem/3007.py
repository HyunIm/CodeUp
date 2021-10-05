# File : 3007.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-05
# Brief : 동적계획법

import itertools
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [list(map(int, input().split())) for _ in range(m)]
a = [0] + list(itertools.accumulate(a))
for i, j in b:
    print(a[j]-a[i-1])
