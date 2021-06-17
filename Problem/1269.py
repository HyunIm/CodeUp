# File : 1269.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-17
# Brief : 단순 반복문

a, b, c, n = map(int, input().split())
for i in range(n-1):
    a = a*b+c
print(a)
