# File : 1253.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 단순 반복문

n = list(map(int, input().split()))
for i in range(min(n), max(n)+1):
    print(i, end=' ')
