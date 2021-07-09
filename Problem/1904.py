# File : 1904.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

def f(b):
    if a>b: return
    f(b-2); return print(b, end=' ')
a, b = map(int, input().split())
f(b if b%2 else b-1)
