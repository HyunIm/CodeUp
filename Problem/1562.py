# File : 1562.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

f = lambda x, y: x if x<y else y
n, m = map(int, input().split())
print(f(n, m))
