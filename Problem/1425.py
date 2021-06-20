# File  : 1425.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 1차원 배열

n, c = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
j = 1
for i in a:
    print(i, end=' ')
    if j==c:
        print()
        j = 0
    j += 1
