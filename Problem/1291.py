# File : 1291.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-09
# Brief : 기초

import math
n = list(map(int, input().split()))
print(math.gcd(math.gcd(n[0], n[1]), n[2]))
