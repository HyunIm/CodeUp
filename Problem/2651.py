# File : 2651.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-03
# Brief : 탐색기반설계

import math
n, k = map(int, input().split())
print(int((math.factorial(n))/((math.factorial(n-k))*(math.factorial(k)))))
