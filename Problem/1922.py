# File : 1922.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-17
# Brief : 기초

def f(x, k):
    if x==1: return k
    elif x%2: return f(3*x+1, k+1)
    else: return f(x//2, k+1)

n = int(input())
print(f(n, 1))
