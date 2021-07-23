# File : 3120.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-23
# Brief : 그리디

a, b = map(int, input().split())
n = abs(a-b); c = 0
while n!=0:
    c += 1
    i = n-10 if n>0 else n+10
    j = n-5 if n>0 else n+5
    k = n-1 if n>0 else n+1
    q, w, e = abs(i), abs(j), abs(k)
    n = i if q<w and q<e else j if w<q and w<e else k
print(c)
