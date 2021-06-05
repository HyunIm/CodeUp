# File : 6079.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-05
# Brief : 종합

n = int(input())
s = 0

for i in range(1, n + 2):
    if s >= n:
        print(i - 1)
        break
    s += i
