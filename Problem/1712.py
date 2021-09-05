# File : 1712.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-05
# Brief : 기초

a, b, k = map(int, input().split())
for i in range(a, k+1, b-a): print(i, end=' ')
