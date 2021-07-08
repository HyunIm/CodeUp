# File : 3016.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-08
# Brief : 구조체 연습

n = int(input())
s = sorted([list(input().split()) for _ in range(n)], key=lambda x:-int(x[1]))
r = [1]*2
for j in range(2, 4):
    t = sorted(s, key=lambda x: -int(x[j]))
    for i in range(n):
        r[j-2] += 1
        if t[i][j]==s[0][j]:
            r[j-2] -= 1
        if t[i]==s[0]:
            break

print(s[0][0], r[0], r[1])
