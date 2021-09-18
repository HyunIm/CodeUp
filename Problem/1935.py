# File : 1935.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-18
# Brief : 기초

def f(a, b):
    if a==b: return a
    elif a>b: return f(a//2, b)
    else: return f(a, b//2)

a, b = map(int, input().split())
print(f(a, b))
