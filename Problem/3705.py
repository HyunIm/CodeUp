# File : 3705.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-06
# Brief : 동적계획법

n = int(input())
a = list(map(int, input().split()))
t = [0] * n
t[0] = a[0]
for i in range(1, n):
    t[i] = max(0, t[i-1]) + a[i]
print(max(t))
