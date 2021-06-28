# File : 1496.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-28
# Brief : 2차원 배열

n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(0, n, 2):
    b.append(min(a[i], a[i+1]))
print(*b)
