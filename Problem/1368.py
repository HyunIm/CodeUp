# File  : 1367.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-19
# Brief : 중첩 반복문

h, k, d = input().split()
h = int(h)
k = int(k)

if d=='R':
    for i in range(1, h+1):
        print(' '*(h-i)+'*'*k)
else:
    for i in range(0, h):
        print(' '*i+'*'*k)
