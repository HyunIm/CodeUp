# File : 1257.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-16
# Brief : 단순 반복문

a, b = map(int, input().split())
a = a if a%2==1 else a+1
for i in range(a, b+1, 2):
    print(i, end=' ')
