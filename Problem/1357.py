# File  : 1357.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-19
# Brief : 중첩 반복문

n = int(input())
a = ['*'*i for i in range(1, n)]
b = ['*'*i for i in range(n, 0, -1)]
for i in a:
    print(i)
for i in b:
    print(i)
