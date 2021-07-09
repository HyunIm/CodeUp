# File : 3704.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

import sys
sys.setrecursionlimit(1000000)
m = {1:1, 2:2, 3:4}
def f(x):
    if x in m: return m[x]
    else:
        m[x]=(f(x-1)+m[x-2]+m[x-3]) % 1000
        return m[x]
print(f(int(input())))
