# File : 1494.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-27
# Brief : 2차원 배열

n, k = map(int, input().split())
d = [0]*(n+1)
a = []

for _ in range(k):
    s, e, u = map(int, input().split())
    d[s-1] = d[s-1]+u
    d[e] = d[e]-u

for i in range(n):
    a.append(sum(d[:i+1]))

for i in range(n):
    print(d[i], end=' ')
print()
print(*a)
