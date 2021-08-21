# File : 2605.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-21
# Brief : DFS/BFS

from collections import deque

def f(x, y):
    if b[x][y]:
        return 0
    b[x][y] = True

    q = deque()
    q.append((x, y))
    v = a[x][y]
    c = 1

    while q:
        x, y = q.popleft()
        for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
            nx = x+i; ny = y+j
            if 0<=nx<7 and 0<=ny<7:
                if b[nx][ny]==False and a[nx][ny]==v:
                    q.append((nx, ny))
                    b[nx][ny] = True
                    c += 1
    return c

a = [list(map(int, input().split())) for _ in range(7)]
b = [[False]*7 for _ in range(7)]
r = 0
for i in range(7):
    for j in range(7):
        if f(i, j)>=3:
            r += 1
print(r)
