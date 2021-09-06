# File : 1721.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-06
# Brief : 기초

import math
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
print('%.2f'%math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2))
