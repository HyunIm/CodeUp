# File : 1673.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-30
# Brief : 기초

import math
a, b, c = map(int, input().split())
print(math.gcd(math.gcd(a, b), c))
