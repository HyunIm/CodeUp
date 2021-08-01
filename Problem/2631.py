# File : 2631.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-01
# Brief : 탐색기반설계

n, k = map(int, input().split())
a = list(map(int, input().split()))
r = c = i = j = 0
while i != n:
    if j==n:
        if r==k: c += 1
        r -= a[i]
        i += 1
        continue
    if r==k:
        c += 1
        r -= a[i]
        i += 1
    elif r<k:
        r += a[j]
        j += 1
    else:
        r -= a[i]
        i += 1
print(c)
