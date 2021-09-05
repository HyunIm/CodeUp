# File : 1708.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-05
# Brief : 기초

n = int(input())
a = list(map(int, input().split()))
b = sorted(a, reverse=True)
for i in a: print(i, b.index(i)+1)
