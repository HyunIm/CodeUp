# File : 1282.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-18
# Brief : 단순 반복문

import math

n = int(input())
k = 0

while True:
    if math.sqrt(n)%1==0:
        break
    n -= 1
    k += 1

print(k, int(math.sqrt(n)))
