# File : 1222.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-15
# Brief : 조건문

import math
a, b, c = map(int, input().split())
d = math.ceil((90-a)/5)
print('win' if b+d>c else 'same' if b+d==c else 'lose')
