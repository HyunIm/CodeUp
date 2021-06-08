# File : 6093.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-08
# Brief : 종합

n = int(input())
a = list(map(int, input().split()))
a.reverse()
for i in a:
    print(i, end=' ')
