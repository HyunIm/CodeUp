# File : 1445.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-11
# Brief : 기초

a = input()
n = list(map(int, input().split()))
m = list(map(int, input().split()))
print(*sorted(n+m))
