# File  : 1420.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 1차원 배열

n = int(input())
a = []
for i in range(n):
    a.append(input().split())
a.sort(key=lambda a: int(a[1]), reverse=True)
print(a[2][0])
