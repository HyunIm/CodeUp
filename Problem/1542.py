# File : 1542.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

def f(x):
    for i in range(2, x):
        if x%i==0:
            return print('composite')
    return print('prime')
n = int(input())
f(n)
