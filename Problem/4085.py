# File : 4085.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-05
# Brief : 2차원 배열

m, n, x, y = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
r = 0
for i in range(0, n-y+1):
    for j in range(0, m-x+1):
        s = 0
        for p in range(y):
            for q in range(x):
                s += a[i + p][j + q]
        if r < s:
            r = s
print(r)
