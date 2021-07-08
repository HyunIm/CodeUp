# File : 1610.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

f = lambda a, s, c: a[s:s+c]
a = input()
s, c = map(int, input().split())
print(f(a, s, c))
