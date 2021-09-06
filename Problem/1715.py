# File : 1715.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-06
# Brief : 기초

import math
a, b = map(int, input().split())
g = math.gcd(a, b)
print(a//g, b//g)
