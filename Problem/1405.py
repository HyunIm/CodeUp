# File  : 1405.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 1차원 배열

n = int(input())
k = input().split()
for i in range(n):
    for j in range(n):
        print(k[(j+i)%n], end=' ')
    print()
