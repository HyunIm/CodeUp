# File : 1902.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

def f(x):
    if x==0: return
    else: print(x); return f(x-1)
f(int(input()))
