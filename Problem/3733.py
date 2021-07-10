# File : 3733.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

import sys
m = {1:1}
def f(n):
    if n in m:
        return m[n]
    if n%2:
        m[n] = 1+f(3*n+1)
        return m[n]
    else:
        m[n] = 1+f(int(n/2))
        return m[n]
a, b = map(int, sys.stdin.readline().split())
for i in range(a, b+1):
    f(i)
if b>5000000:
    for i in range(b+1, 5000000, -1):
        f(i)
print(int(sorted(m, key=lambda x:-m.get(x))[0]), m.get(int(sorted(m, key=lambda x:-m.get(x))[0])))
