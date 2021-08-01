# File : 2628.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-01
# Brief : 탐색기반설계

a, b = sorted(map(int, input().split()))
c = 0
for i in map(int, input().split()):
    if a < i < b: c += 1
print('cross' if c==1 else 'not cross')
