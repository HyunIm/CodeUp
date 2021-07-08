# File : 1620.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

def f(x):
    while len(x)!=1:
        x = str(sum(map(int, str(x))))
    return x
n = input()
print(f(n))
