# File  : 1411.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 1차원 배열

n = int(input())
a = [0]*n
for _ in range(n-1):
    a[int(input())-1] = 1
print(a.index(0)+1)
