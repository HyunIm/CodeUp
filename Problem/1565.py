# File : 1565.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

import math
from decimal import Decimal
f = lambda x, y: int(x*y/Decimal(math.gcd(x, y)))
a, b = map(int, input().split())
print(f(a, b))
