# File : 1430.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 1차원 배열

import sys
c = {}
n = sys.stdin.readline()
for i in sys.stdin.readline().split(): c[i] = 1
m = sys.stdin.readline()
for j in sys.stdin.readline().split():
    if j in c: print(1, end=' ')
    else: print(0, end=' ')
