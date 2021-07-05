# File : 1525.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-05
# Brief : 2차원 배열

def f1(i, j, w):
    if w==0:
        return 0
    t = a[i][j]
    if t != -1:
        a[i][j] = -2
        if t > 0:
            t += 1
            f1(i, j, t); f2(i, j, t); f3(i, j, t); f4(i, j, t);
        if j>0:
            f1(i, j-1, w-1)

def f2(i, j, w):
    if w==0:
        return 0
    t = a[i][j]
    if t != -1:
        a[i][j] = -2
        if t > 0:
            t += 1
            f1(i, j, t); f2(i, j, t); f3(i, j, t); f4(i, j, t);
        if j<9:
            f2(i, j+1, w-1)

def f3(i, j, w):
    if w==0:
        return 0
    t = a[i][j]
    if t != -1:
        a[i][j] = -2
        if t > 0:
            t += 1
            f1(i, j, t); f2(i, j, t); f3(i, j, t); f4(i, j, t);
        if i>0:
            f3(i-1, j, w-1)

def f4(i, j, w):
    if w==0:
        return 0
    t = a[i][j]
    if t != -1:
        a[i][j] = -2
        if t > 0:
            t += 1
            f1(i, j, t); f2(i, j, t); f3(i, j, t); f4(i, j, t);
        if i<9:
            f4(i+1, j, w-1)

a = [list(map(int, input().split())) for _ in range(10)]
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
c = []

for i in range(10):
    for j in range(10):
        if a[i][j] > 0:
            w = a[i][j]+1
            f1(i, j, w); f2(i, j, w); f3(i, j, w); f4(i, j, w);

for i in range(n):
    if a[p[i][0]-1][p[i][1]-1] != -2:
        a[p[i][0]-1][p[i][1]-1] = i+1
        c.append('player %d survive'%(i+1))
    else:
        c.append('player %d dead'%(i+1))

for i in a:
    print(*i)
print('Character Information')
for i in c:
    print(i)
