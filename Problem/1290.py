# File : 1290.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-09
# Brief : 기초

n = int(input())
r = 0
for i in range(1, n):
    if n%i==0: r += 1
print(r)
