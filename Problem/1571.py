# File : 1571.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

import bisect
f = lambda x: bisect.bisect_right(a, x)+1
n = input()
a = list(map(int, input().split()))
k = int(input())
print(f(k))
