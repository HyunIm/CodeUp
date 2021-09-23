# File : 2012.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-24
# Brief : 중급

a, b = map(int, input().split())
r = 0
for i in range(a, b+1):
    i = str(i)
    r += i.count('1')
print(r)
