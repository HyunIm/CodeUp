# File : 4713.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-27
# Brief : 그리디

def f():
    c = []
    for i in d:
        if i[0]<sm or (i[0]==sm and i[1]<=sd):
            c.append(i)
    c.sort(key=lambda x: (-x[2], -x[3]))
    return c[0]

n = int(input())
d = sorted([list(map(int, input().split())) for _ in range(n)])
m = {3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
sm = fm = 3; sd = fd = 1
r = 0

for i in range(n):
    if d[i][0] < 3:
        d[i][0] = 3
        d[i][1] = 1
    if d[i][2] == 12:
        d[i][3] = 1

while (not (fm==12 and fd==1)):
    r += 1
    sm, sd, fm, fd = f()
print(r)
