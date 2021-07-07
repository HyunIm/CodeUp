# File : 1557.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

def f(x):
    c = 0
    for i in range(1, x+1):
        if x%i==0:
            c += 1
    return c
n = int(input())
print(f(n))
