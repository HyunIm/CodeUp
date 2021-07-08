# File : 3019.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-08
# Brief : 구조체 연습

n = int(input())
s = sorted([list(input().split()) for _ in range(n)], key=lambda x:(int(x[1]), x[2], x[3], x[0]))
for i in s: print(i[0])
