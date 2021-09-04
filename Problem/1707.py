# File : 1707.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-04
# Brief : 기초

import bisect
n = sorted(list(map(int, input().split())))
x = round(sum(n)/10, 1)
y = bisect.bisect_left(n, x)
print(x)
print(10-y, y)
