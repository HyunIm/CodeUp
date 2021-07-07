# File : 1535.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

f = lambda a: a.index(max(a))+1
n = input()
a = list(map(int, input().split()))
print(f(a))
