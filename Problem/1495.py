# File : 1495.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-27
# Brief : 2차원 배열

n, m, k = map(int, input().split())
d = [[0]*(m+1) for _ in range(n+1)]
s = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    x1, y1, x2, y2, u = map(int, input().split())
    if x1<=n and y1<=m:
        d[x1][y1] = d[x1][y1]+u
    if x2<=n and y2<=m:
        d[x2+1][y2+1] = d[x2+1][y2+1]+u
    if x1 <= n and y2 <= m:
        d[x1][y2+1] = d[x1][y2+1]-u
    if x2 <= n and y1 <= m:
        d[x2+1][y1] = d[x2+1][y1]-u

for i in range(1, n+1):
    for j in range(1, m+1):
        s[i][j] = d[i-1][j-1] + s[i][j-1] + s[i-1][j] - s[i-1][j-1]

for i in range(n):
    for j in range(m):
        print(d[i][j], end=' ')
    print()
print()
for i in range(1, n+1):
    for j in range(1, m+1):
        print(s[i][j], end=' ')
    print()
