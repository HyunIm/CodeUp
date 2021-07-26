# File : 4040.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-26
# Brief : 그리디

def f(i):
    c = [0]*m
    for j in range(m):
        for k in range(i, t):
            if a[k][j] == 'O': c[j] += 1
            else: break
    return max(c)

n, m = map(int, input().split())
a = [input() for _ in range(n)]
s, t = map(int, input().split())
s-=1; t-=1
r=d=-1

while s<t:
    d = f(s)
    if d==0:
        r = -1
        break
    s += d
    r += 1

print(r)
