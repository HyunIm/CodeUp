# File : 1807.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

m = {1:1}
def f(n):
    if n in m: return m[n]
    if n%2:
        m[n] = 1+f(3*n+1)
        return m[n]
    else:
        m[n] = 1+f(int(n/2))
        return m[n]
a, b = map(int, input().split())
s = []
for i in range(a, b+1): f(i)
print(int(sorted(m, key=lambda x:-m.get(x))[0]), m.get(int(sorted(m, key=lambda x:-m.get(x))[0])))
