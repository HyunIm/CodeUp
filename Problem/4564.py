# File : 4564.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-11
# Brief : 재귀함수

import sys
n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]
m = [s[0], s[0]+s[1], max(s[0], s[1])+s[2]]
for i in range(3, n):
    m.append(max(s[i-1]+m[i-3], m[i-2])+s[i])
print(m[-1])
