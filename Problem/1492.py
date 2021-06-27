# File : 1492.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-27
# Brief : 2차원 배열

n = int(input())
a = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(a[i]+s[i])
s.remove(0)
print(*s)
