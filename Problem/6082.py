# File : 6082.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-05
# Brief : 종합

n = int(input())
s = [3, 6, 9]
for i in range(1, n + 1):
    if i % 10 in s:
        print('X', end = ' ')
    else:
        print(i, end = ' ')
