# File : 4751.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-08
# Brief : 구조체 연습

n = int(input())
s = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(-x[2], -x[0]))
c, f = [0]*3, 3
for i in s:
    if not f: break
    if c.count(i[0]) != 2:
        print(i[0], i[1])
        c[f-1] = i[0]
        f -= 1
