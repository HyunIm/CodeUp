# File : 1861.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-12
# Brief : 기초

def f(x):
    print(*(a := [1] if x==1 else [1] + list(map(sum, zip((p := f(x-1))[:-1], p[1:]))) + [1]))
    return a

f(int(input()))
