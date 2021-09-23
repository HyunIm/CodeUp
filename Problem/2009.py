# File : 2009.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-23
# Brief : 중급

n, k = map(int, input().split())
r = 0
while n >= k:
    t = n//k
    n %= k
    n += t
    r += t
print(r)
