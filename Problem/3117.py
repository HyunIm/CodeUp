# File : 3117.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-06
# Brief : 스택

n = int(input())
s = []
for _ in range(n):
    i = int(input())
    if i: s.append(i)
    else: s.pop()
print(sum(s))