# File : 1936.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-19
# Brief : 기초

def f(a, b):
    if a==b: return 0
    elif a>b: return f(a//2, b)+1
    else: return f(a, b//2)+1

a, b = map(int, input().split())
print(f(a, b))
