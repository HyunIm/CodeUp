# File : 3129.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-07
# Brief : 스택

n = input()
s = []
r = 0
for i in n:
    if i=='(': s.append(i)
    else:
        if s: s.pop()
        else: r = 1; break
print('bad' if (s or r) else 'good')
