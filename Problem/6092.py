# File : 6092.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-08
# Brief : 종합

n = int(input())
a = list(map(int, input().split()))
d = [0] * 24

for i in range(n):
    d[a[i]] += 1

del d[0]
for i in d:
    print(i, end=' ')
