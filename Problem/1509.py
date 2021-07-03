# File : 1509.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-03
# Brief : 2차원 배열

a = [list(map(int, input().split())) for _ in range(10)]
o = list(map(int, input().split()))

for i in range(10):
    if o[i] == 1:
        t = 'safe'
        for j in range(9, -1, -1):
            if a[j][i] > 0:
                t = 'crash'
                break
            elif a[j][i] < 0:
                t = 'fall'
                break
        print(i+1, t)
