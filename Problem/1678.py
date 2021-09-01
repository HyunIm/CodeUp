# File : 1678.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-01
# Brief : 기초

a = [list(map(int, input().split())) for _ in range(5)]
r = 0
for i in range(3):
    for j in range(3):
        s = 0
        for x, y in ((0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)):
            s += a[i+x][j+y]
        r = max(r, s)
print(r)
