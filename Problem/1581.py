# File : 1581.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

myswap = lambda x, y: (y, x) if x>y else (x, y)
a, b = map(int, input().split())
a, b = myswap(a, b)
print(a, b)
