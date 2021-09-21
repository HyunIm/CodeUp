# File : 2004.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-21
# Brief : 중급

x, y = map(int, input().split())
a, b = map(int, input().split())
for i in range(x):
    for _ in range(a):
        for j in range(y):
            for _ in range(b):
                if (i+j)%2: print('.', end='')
                else: print('X', end='')
        print()
