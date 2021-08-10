# File : 1415.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-11
# Brief : 기초

n = sorted(list(map(int, input().split())), reverse=True)
for i in n:
    if i%2: print(i, end=' '); break
for i in n:
    if i%2==0: print(i); break
