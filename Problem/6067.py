# File : 6067.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-04
# Brief : 구조

i = int(input())
if i % 2 == 0:
    if i < 0:
        print('A')
    else:
        print('C')
else:
    if i < 0:
        print('B')
    else:
        print('D')
