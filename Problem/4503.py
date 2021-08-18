# File : 4503.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-18
# Brief : DFS/BFS

import sys
input = sys.stdin.readline
def f(s):
    global r
    r += 1
    v[s] = False
    for i in a[s]:
        if v[i]: f(i)
n = int(input())
m = int(input())
a = [[] for _ in range(n+1)]
v = [True]*(n+1)
r = -1
for _ in range(m):
    i, j = map(int, input().split())
    a[i].append(j)
    a[j].append(i)
f(1)
print(r)
