# File : 3301.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-23
# Brief : 그리디

n = int(input())
a, b = map(int, input().split())
c = int(input())
d = sorted([int(input()) for _ in range(n)], reverse=True)

for i in d:
    if i/b > c/a:
        c += i
        a += b

print(int(c/a))
