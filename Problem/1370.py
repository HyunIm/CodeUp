# File  : 1370.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-06-20
# Brief : 중첩 반복문

h, r = map(int, input().split())
for i in range(r):
    for j in range(h-1):
        print(' '*j+'*')
    for j in range(h-1, -1, -1):
        print(' '*j+'*')
