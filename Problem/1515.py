# File : 1515.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-03
# Brief : 2차원 배열

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def f1(i, j):
    c = 0
    for l in range(8):
        if -1<i+dx[l]<25 and -1<j+dy[l]<25:
            if a[i+dx[l]][j+dy[l]]==1:
                c += 1
    return 1 if c==3 else 0
def f2(i, j):
    c = 0
    for l in range(8):
        if -1<i+dx[l]<25 and -1<j+dy[l]<25:
            if a[i+dx[l]][j+dy[l]]==1:
                c += 1
    return 0 if c<=1 or c>=4 else 1

a = [list(map(int, input().split())) for _ in range(25)]
for i in range(25):
    for j in range(25):
        if a[i][j]:
            print(f2(i, j), end=' ')
        else:
            print(f1(i, j), end=' ')
    print()
