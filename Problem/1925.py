# File : 1925.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-17
# Brief : 기초

import math
n, r = map(int, input().split())
f = math.factorial
print(f(n)//(f(r)*f(n-r)))
