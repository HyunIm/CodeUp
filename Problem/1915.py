# File : 1915.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-09
# Brief : 재귀함수

def f(n):
    if n==1 or n==2: return 1
    else: return f(n-1)+f(n-2)
print(f(int(input())))
