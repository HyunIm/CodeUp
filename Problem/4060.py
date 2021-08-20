# File : 4060.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-18
# Brief : DFS/BFS

def on(x, y):
    if a[x][y] == 0:
        a[x][y] = 1
        for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
            if 0<=x+i<m and 0<=y+j<n:
                on(x+i, y+j)
        return True
    return False

def off(x, y):
    if b[x][y] == 1:
        b[x][y] = 0
        for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
            if 0<=x+i<m and 0<=y+j<n:
                off(x+i, y+j)
        return True
    return False

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
b = [[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        b[i][j] = a[i][j]
c = d = 0

for i in range(m):
    for j in range(n):
        if on(i, j):
            c += 1
for i in range(m):
    for j in range(n):
        if off(i, j):
            d += 1
print(c, d)
