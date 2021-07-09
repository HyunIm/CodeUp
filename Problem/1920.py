# File : 1920.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

def f(n):
    if n<2:
        return print(n,end='')
    else:
        f(int(n/2))
        return print(n%2,end='')
f(int(input()))
