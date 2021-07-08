# File : 3109.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-08
# Brief : 구조체 연습

import sys
n = int(sys.stdin.readline())
s = {}
for _ in range(n):
    t = sys.stdin.readline().split()
    t[1] = int(t[1])
    if t[0] == 'I':
        if t[1] in s:
            s[t[1]].append(t[2])
        else:
            s[t[1]] = [t[2]]
    else:
        try:
            s[t[1]].pop()
            if not len(s[t[1]]):
                del s[t[1]]
        except: continue
s = sorted(s.items())
r = map(int, sys.stdin.readline().split())
f = 5
for i in r:
    for j in range(len(s[i-1][1])-1, -1, -1):
        if f == 0:
            break
        print(s[i-1][0], s[i-1][1][j])
        f -= 1
