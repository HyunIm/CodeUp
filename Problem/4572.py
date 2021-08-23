# File : 4572.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-22
# Brief : DFS/BFS

from collections import deque

def bfs(x, y):
    if a[x][y] == 1:
        return False
    c = 1
    a[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
            nx = x+i; ny = y+j
            if 0<=nx<m and 0<=ny<n:
                if a[nx][ny] == 0:
                    a[nx][ny] = 1
                    q.append((nx, ny))
                    c += 1
    return c

m, n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(k)]
r = 0
ra = []

a = [[0]*n for _ in range(m)]
for l in range(k):
    for i in range(t[l][0], t[l][2]):
        for j in range(t[l][1], t[l][3]):
            a[j][i] = 1

for i in range(m):
    for j in range(n):
        result = bfs(i, j)
        if result:
            r += 1
            ra.append(result)

print(r)
print(*sorted(ra))
