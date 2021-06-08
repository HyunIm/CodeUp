# File : 6091.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-08
# Brief : 종합

a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0:
    d += 1
print(d)
