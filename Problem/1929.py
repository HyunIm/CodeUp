# File : 1929.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

def f(n):
    if n==1: return
    if n%2: f(3*n+1); return print(3*n+1)
    else: f(int(n/2)); return print(int(n/2))
n = int(input())
f(n)
print(n)
