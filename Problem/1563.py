# File : 1563.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

f = lambda x, y, z: (x+y+z)-max(x,y,z)-min(x,y,z)
n, m, x = map(int, input().split())
print(f(n, m, x))
