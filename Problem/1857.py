# File : 1857.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

import math
n, r = map(int, input().split())
f = math.factorial
print(f(n)//(f(n-r)*f(r)) if n>=r else 0)
