# File : 1564.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

import math
f = lambda x, y: math.lcm(x, y)
a, b = map(int, input().split())
print(f(a, b))
