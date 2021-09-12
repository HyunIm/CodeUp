# File : 1858.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

import math
n, r = map(int, input().split())
n-=1; r-=1;
f = math.factorial
print(f(n)//(f(n-r)*f(r)))
