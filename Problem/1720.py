# File : 1720.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-06
# Brief : 기초

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
f = True
for i in range(n):
    if min(a[i][:-1]) != a[i][-1]:
        print(i+1, min(a[i][:-1]))
        f = False
        break
if f: print(-1)
