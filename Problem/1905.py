# File : 1905.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n!=1: return f(n-1)+n
    else: return 1
print(f(int(input())))
