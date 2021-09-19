# File : 1960.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-19
# Brief : 기초

n = int(input())
r = 2
for i in range(2, n+1):
    r += i
    r %= 137
print(0 if r==0 else r)
