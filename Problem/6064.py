# File : 6064.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-03
# Brief : 연산

a, b, c = map(int, input().split())
print((a if a < b else b) if ((a if a < b else b) < c) else c)
