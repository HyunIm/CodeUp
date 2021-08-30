# File : 1676.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-30
# Brief : 기초

n = int(input())
a = [int(input()) for _ in range(n)]
b = sorted(a, reverse=True)
r = {}
for i in range(n):
    if b[i] not in r: r[b[i]] = i+1
for i in a: print(r[i])
