# File : 6086.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-06
# Brief : 종합

n = int(input())
s = 0

for i in range(n + 2):
    if n <= s:
        print(s)
        break
    s += i
