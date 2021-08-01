# File : 2633.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-01
# Brief : 탐색기반설계

import bisect
n, k = input().split()
print(bisect.bisect_left(list(map(int, input().split())), int(k))+1)
