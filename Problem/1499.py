# File : 1499.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-28
# Brief : 2차원 배열

n, g = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(0, n, g):
    b.append(max(a[i:i+g]))
print(*b)
