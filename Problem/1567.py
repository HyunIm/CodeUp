# File : 1567.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

f = lambda x, y: sum(k[a-1:b])
n = input()
k = list(map(int, input().split()))
a, b = map(int, input().split())
print(f(a, b))
