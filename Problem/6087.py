# File : 6087.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-06
# Brief : 종합

n = int(input())

for i in range(1, n + 1):
    if (i % 3 == 0):
        continue
    print(i, end = ' ')
