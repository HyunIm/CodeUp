# File : 3170.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-08
# Brief : 구조체 연습

import sys
n, m = map(int, sys.stdin.readline().split())
s = {}
for _ in range(n):
    t = sys.stdin.readline().split()
    try: s[t[0]] += int(t[1])
    except: s[t[0]] = int(t[1])
for _ in range(m):
    try: print(s[sys.stdin.readline().rstrip()])
    except: print(0)
