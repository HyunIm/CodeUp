# File : 1524.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-04
# Brief : 2차원 배열

a = [list(map(int, input().split())) for _ in range(9)]
r, c = map(int, input().split())
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
p = 0
for i in range(8):
    if -1<r+dx[i]-1<9 and -1<c+dy[i]-1<9:
        p += a[r+dx[i]-1][c+dy[i]-1]

print(-1 if a[r-1][c-1] else p)
