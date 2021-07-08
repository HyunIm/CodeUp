# File : 1615.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-07
# Brief : 함수

d = lambda x: sum(map(int, str(x)))+x
a, b = map(int, input().split())
n = [True]*(b+1)
s = 0

for i in range(1, b+1):
    try: n[d(i)] = False
    except: continue

for i in range(a, b+1):
    if n[i]:
        s += i

print(s)
