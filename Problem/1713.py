# File : 1713.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-05
# Brief : 기초

a, b = map(int, input().split())
r = 0
s = a+(3-a%3) if a%3 else a
e = b-(b%3) if b%3 else b
r += ((e-s)//3+1)*(s+e)//2
s = a+(4-a%4) if a%4 else a
e = b-(b%4) if b%4 else b
r -= ((e-s)//4+1)*(s+e)//2
print(r)
