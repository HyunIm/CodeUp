# File : 1230.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 조건문

n = list(map(int, input().split()))
p = 0
for i in n:
    if i<=170:
        print('CRASH', i)
        break
    p += 1
print('PASS' if p==3 else '')

