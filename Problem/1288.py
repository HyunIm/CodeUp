# File : 1288.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-09
# Brief : 기초

import math
f = math.factorial
n, r = map(int, input().split())
print(int((f(n))/((f(r))*f(n-r))))
