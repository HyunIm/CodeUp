# File : 6066.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-04
# Brief : 구조

n = map(int, input().split())
for i in n:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')
