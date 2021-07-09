# File : 1912.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

def f(n):
    if n==1: return 1
    else: return f(n-1)*n
print(f(int(input())))
