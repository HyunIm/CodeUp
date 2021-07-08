# File : 1805.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-08
# Brief : 구조체 연습

n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)])
for i in a: print(*i)
