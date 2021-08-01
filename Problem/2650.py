# File : 2650.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-01
# Brief : 탐색기반설계

def f(m, n):
    while n!=0:
        t = m%n
        m, n = n, t
    return abs(m)

a, b, c = sorted(map(int, input().split()))
d = f(c, b)
print(f(max(a, d), min(a, d)))

