# File : 1560.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

f = lambda x, y: x-y if x>y else y-x
n, m = map(int, input().split())
print(f(n, m))
