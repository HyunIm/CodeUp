# File : 4012.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-08
# Brief : 구조체 연습

n = int(input())
a = list(map(int, input().split()))
c = sorted(a.copy(), reverse=True)
for i in a:
    r = 0
    for j in c:
        r += 1
        if i == j:
            break
    print(i, r)
