# File : 1551.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

def f(x):
    try:
        return a.index(x)+1
    except:
        return -1
n = input()
a = list(input().split())
k = input()
print(f(k))
