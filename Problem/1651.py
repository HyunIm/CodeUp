# File : 1651.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-30
# Brief : 기초

w, h, n = map(int, input().split())
for i in [input() for _ in range(n)]:
    for y in range(h):
        for j in i:
            for x in range(w):
                print(j, end='')
        print()
