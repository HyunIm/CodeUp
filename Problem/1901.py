# File : 1901.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

def f(x):
    if x==0: return
    else: f(x-1); return print(x)
f(int(input()))
