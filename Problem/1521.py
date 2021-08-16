# File : 1521.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-16
# Brief : 기초

k, n = map(int, input().split())
a = []
c = 0

for _ in range(k):
    r = list(map(int, input().split()))
    for i in range(k):
        if r[i] > -1: r[i] += n
    a.append(r)

for i in a:
    for j in i:
        if 0<=j<6: c += 1
print(c)
