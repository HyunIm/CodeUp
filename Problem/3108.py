# File : 3108.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-08
# Brief : 구조체 연습

n = int(input())
s = []
for _ in range(n):
    t = input().split()
    if t[0] == 'I': s.append(t[1:3])
    else:
        for i in s.copy():
            if i[0]==t[1]: s.remove(i)
s.sort(key=lambda x:int(x[0]))
r = map(int, input().split())
for i in r:
    print(*s[i-1])