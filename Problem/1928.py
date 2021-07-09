# File : 1928.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

def f(n):
    if n==1: return
    if n%2: print(3*n+1); return f(3*n+1)
    else: print(int(n/2)); return f(int(n/2))
n = int(input())
print(n)
f(n)
