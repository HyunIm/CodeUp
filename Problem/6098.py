# File : 6098.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-11
# Brief : 종합

a = [0] * 10
for i in range(10):
    a[i] = list(map(int, input().split()))

x, y = 1, 1
while True:
    if a[x][y] == 0:
        a[x][y] = 9
    elif a[x][y] == 2:
        a[x][y] = 9
        break

    if (a[x][y+1] == 1 and a[x+1][y] == 1) or (x == 9 and y == 9):
        break

    if a[x][y + 1] != 1:
        y += 1
    elif a[x+1][y] != 1:
        x += 1

for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print()
